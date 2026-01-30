# Data Labeling Presets

# Common Fields (Applied to all sources)
# "exclude" is usually placed at the top
# "remarks" is usually placed at the bottom
COMMON_FIELDS_TOP = [
    {
        "name": "is_excluded",
        "label_key": "lbl_is_excluded",
        "type": "single",
        "options": ["否 (No)", "是 (Yes)"],
        "scores": {0: 0, 1: 1} # 0=Keep, 1=Exclude (Logic handled by user interpretation or analysis)
    }
]

COMMON_FIELDS_BOTTOM = [
    {
        "name": "remarks",
        "label_key": "lbl_remarks",
        "type": "text",
        "options": []
    }
]

# Source Specific Fields
VIDEO_FIELDS = [
    {
        "name": "mDiscern_Score",
        "label_key": "lbl_mdiscern",
        "type": "multi",
        "options": [
            "1. Is the aim clear? (主题明晰性)",
            "2. Are reliable sources cited? (信息可靠性)",
            "3. Is the date of publication cited? (信息时效性)",
            "4. Is the information balanced/unbiased? (信息公正性)",
            "5. Are areas of uncertainty mentioned? (信息不确定性)"
        ],
        "scores": None # Handled by special logic in LabelWorkspaceWidget if needed, or just sum count
    },
    {
        "name": "JAMA_Score",
        "label_key": "lbl_jama",
        "type": "multi",
        "options": [
            "1. Authorship (作者信息)",
            "2. Attribution (参考文献)",
            "3. Currency (日期)",
            "4. Disclosure (利益冲突)"
        ],
        "scores": None
    },
    {
        "name": "GQS_Score",
        "label_key": "lbl_gqs",
        "type": "single",
        "options": ["差 (Poor)", "较差 (Fair)", "一般 (Good)", "较好 (Very Good)", "好 (Excellent)"],
        "scores": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    }
]

SOURCE_PRESETS = {
    "video": VIDEO_FIELDS
}
