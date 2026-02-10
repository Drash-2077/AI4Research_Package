# Scientific Color Palettes
# Based on ggsci and other scientific visualization libraries

SCIENTIFIC_PALETTES = {
    # Journal / Publisher Palettes
    "NPG (Nature)": ['#E64B35', '#4DBBD5', '#00A087', '#3C5488', '#F39B7F', '#8491B4', '#91D1C2', '#DC0000', '#7E6148', '#B09C85'],
    "AAAS (Science)": ['#3B4992', '#EE0000', '#008B45', '#631879', '#5F559B', '#A20056', '#808180', '#1B1919'],
    "NEJM (New England)": ['#BC3C29', '#0072B5', '#E18727', '#20854E', '#7876B1', '#6F99AD', '#FFDC91', '#EE4C97'],
    "Lancet": ['#00468B', '#ED0000', '#42B540', '#0099B4', '#925E9F', '#FDAF91', '#AD002A', '#ADB6B6'],
    "JAMA": ['#374E55', '#DF8F44', '#00A1D5', '#B24745', '#79AF97', '#6A6599', '#80796B'],
    "JCO": ['#008392', '#50274C', '#BF1E2E', '#EFA929', '#0C6C59', '#D5A47B', '#808080'],
    "UCSC (Genome Browser)": ['#ff0000', '#ff9900', '#00ff00', '#0000ff', '#9900cc', '#996600', '#666666', '#ffff00'],
    "LocusZoom": ['#D43F3A', '#EEA236', '#5CB85C', '#46B8DA', '#357EBD', '#9632B8', '#B8B8B8'],
    "IGV": ['#5050FF', '#CE3D32', '#749B58', '#F0E685', '#466983', '#BA6338', '#5DB1DD', '#802268', '#6BD76B', '#D595A7', '#924822', '#837B8D'],
    "D3 (Category10)": ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
    "Okabe-Ito (Colorblind Safe)": ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000'],
    "Tableau 10": ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC'],
    
    # Standard Seaborn/Matplotlib Palettes
    "Deep": "deep",
    "Muted": "muted",
    "Pastel": "pastel",
    "Bright": "bright",
    "Dark": "dark",
    "Colorblind": "colorblind",
    
    # Continuous Colormaps (Merged)
    "Viridis": "viridis",
    "Magma": "magma",
    "Inferno": "inferno",
    "Plasma": "plasma",
    "CoolWarm": "coolwarm",
    "RdBu (Red-Blue)": "RdBu_r",
    "Spectral": "Spectral_r",
    "Blues": "Blues",
    "Reds": "Reds",
    "Greens": "Greens",
    "Greys": "Greys",
    "Oranges": "Oranges",
    "Purples": "Purples",
    "YlOrBr": "YlOrBr",
    "YlGnBu": "YlGnBu"
}

# Kept for backward compatibility if needed, but aliases to main list keys or values
HEATMAP_CMAPS = {k: v for k, v in SCIENTIFIC_PALETTES.items() if isinstance(v, str)}
