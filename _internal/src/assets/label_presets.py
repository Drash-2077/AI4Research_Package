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
        "scores": {0: 0, 1: 1}, # 0=Keep, 1=Exclude (Logic handled by user interpretation or analysis)
        "description": "Determine if the video is irrelevant, duplicated, or invalid and should be excluded from analysis."
    }
]

COMMON_FIELDS_BOTTOM = [
    {
        "name": "remarks",
        "label_key": "lbl_remarks",
        "type": "text",
        "options": [],
        "description": "Any additional notes, observations, or key takeaways from the video content."
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
        "scores": None, # Handled by special logic in LabelWorkspaceWidget if needed, or just sum count
        "description": "mDISCERN 评分标准 (满足得1分，不满足得0分):\n1. 主题明晰性: 0分-主题模糊；1分-主题清晰明确，开篇即知核心目标。\n2. 信息可靠性: 0分-无/不可靠来源；1分-引用可靠来源(文献/指南/专家)且可追溯。\n3. 信息时效性: 0分-无日期/过时；1分-标注日期且信息有效(近3年)。\n4. 信息公正性: 0分-片面/偏见；1分-客观平衡，说明局限性。\n5. 信息不确定性: 0分-未提及不确定性；1分-主动提及不确定领域/数据局限。"
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
        "scores": None,
        "description": "JAMA 评分标准 (满足得1分，不满足得0分):\n1. 作者资质: 0分-未标注；1分-完整标注姓名、资质及机构。\n2. 信息来源: 0分-未提及/模糊；1分-明确引用文献/指南/权威机构。\n3. 内容时效性: 0分-未标注/过时；1分-标注日期且基于最新证据(近3年)。\n4. 利益冲突: 0分-未提及；1分-明确披露利益关系。"
    },
    {
        "name": "GQS_Score",
        "label_key": "lbl_gqs",
        "type": "single",
        "options": ["差 (Poor)", "较差 (Fair)", "一般 (Good)", "较好 (Very Good)", "好 (Excellent)"],
        "scores": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
        "description": "GQS 总体质量评分标准 (1-5分):\n1分 (差): 质量差，信息流畅度弱，大部分重要信息缺失，对患者完全无用。\n2分 (较差): 总体质量低，信息流畅度差，重要主题缺失多，价值极有限。\n3分 (一般): 中等质量，部分讨论充分部分不足，对患者有一定帮助。\n4分 (较好): 良好质量，信息流畅度好，涵盖大部分重要主题，对患者有用。\n5分 (好): 优秀质量，信息流畅度极佳，涵盖所有重要主题，对患者非常有用。"
    }
]

SOURCE_PRESETS = {
    "video": VIDEO_FIELDS
}
