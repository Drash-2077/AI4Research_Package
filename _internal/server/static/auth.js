// Auth & Quota Management

// Auth Server URL (Will be fetched from config)
let AUTH_API_BASE = ""; 

const Auth = {
    token: localStorage.getItem('access_token'),
    user: null,
    quota: null,
    onUserChange: null, // Callback (user) => {}
    onQuotaChange: null, // Callback (quota) => {}

    getHeaders: function() {
        const headers = {
            'Content-Type': 'application/json'
        };
        if (this.token) {
            headers['Authorization'] = `Bearer ${this.token}`;
        }
        return headers;
    },

    login: async function(username, password) {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        // Use original fetch to avoid recursion loop or interception issues during login
        const response = await originalFetch(`${AUTH_API_BASE}/auth/token`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || 'Login failed');
        }

        const data = await response.json();
        this.token = data.access_token;
        localStorage.setItem('access_token', this.token);
        await this.fetchCurrentUser();
        return true;
    },

    register: async function(username, password, email) {
        // Use original fetch
        const response = await originalFetch(`${AUTH_API_BASE}/auth/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password, email })
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || 'Registration failed');
        }

        const data = await response.json();
        this.token = data.access_token;
        localStorage.setItem('access_token', this.token);
        await this.fetchCurrentUser();
        return true;
    },

    logout: function() {
        this.token = null;
        this.user = null;
        this.quota = null;
        localStorage.removeItem('access_token');
        if (this.onUserChange) this.onUserChange(null);
        if (this.onQuotaChange) this.onQuotaChange(null);
    },

    fetchCurrentUser: async function() {
        if (!this.token) {
             if (this.onUserChange) this.onUserChange(null);
             return;
        }
        try {
            // Use window.fetch (interceptor handles headers)
            const response = await window.fetch(`${AUTH_API_BASE}/users/me`, {
                headers: { 'Content-Type': 'application/json' } 
            });
            if (response.ok) {
                this.user = await response.json();
                if (this.onUserChange) this.onUserChange(this.user);
                await this.fetchQuota();
            } else {
                console.error("Fetch user failed", response.status);
                // If token invalid/expired, or server error, logout to clear loading state
                this.logout();
            }
        } catch (e) {
            console.error("Fetch user error", e);
            // Network error or other exception - also logout to prevent hanging
            this.logout();
        }
    },

    fetchQuota: async function() {
        if (!this.token) return;
        try {
            const response = await window.fetch(`${AUTH_API_BASE}/quota/status`, {
                 headers: { 'Content-Type': 'application/json' }
            });
            if (response.ok) {
                this.quota = await response.json();
                if (this.onQuotaChange) this.onQuotaChange(this.quota);
            }
        } catch (e) {
            console.error(e);
        }
    },

    init: async function() {
        try {
            // Fetch Config to get Auth Server URL
            const res = await originalFetch('/api/data/config');
            const config = await res.json();
            if (config.auth_server_url) {
                AUTH_API_BASE = config.auth_server_url;
                // Remove trailing slash if present
                if (AUTH_API_BASE.endsWith('/')) {
                    AUTH_API_BASE = AUTH_API_BASE.slice(0, -1);
                }
            } else {
                console.warn("No auth_server_url in config, defaulting to local relative path (legacy mode)");
            }
        } catch (e) {
            console.error("Failed to load config for Auth init:", e);
        }

        this.fetchCurrentUser();
    }
};

// --- Intercept Fetch ---
const originalFetch = window.fetch;
window.fetch = async function(url, options = {}) {
    // Add auth header if token exists
    const token = localStorage.getItem('access_token');
    
    // Skip if request is to auth endpoints (handled explicitly in login/register) but generally safe to add header
    // But login uses FormData, so don't force Content-Type json
    
    if (token) {
        if (!options.headers) options.headers = {};
        
        // Handle Headers object vs plain object
        if (options.headers instanceof Headers) {
             if (!options.headers.has('Authorization')) {
                 options.headers.set('Authorization', `Bearer ${token}`);
             }
        } else {
             if (!options.headers['Authorization']) {
                 options.headers['Authorization'] = `Bearer ${token}`;
             }
        }
    }
    
    // Call original
    const response = await originalFetch(url, options);
    
    // Check 401
    if (response.status === 401) {
        // Token expired or invalid
        if (token) {
             Auth.logout(); 
        }
    }
    
    // Auto Refresh Quota on successful POST (consumption)
    // Filter out auth endpoints
    if (options.method === 'POST' && response.ok && token) {
        const u = url.toString();
        if (!u.includes('/auth/')) {
            // Debounce slightly
            setTimeout(() => Auth.fetchQuota(), 500);
        }
    }
    
    return response;
};

window.Auth = Auth;
