import numpy as np

def generate_environment_and_followup():
    environments = ["병실", "ICU", "수술실", "응급실"]
    followup_plans = ["MRI 재검", "신경과 협진", "재활 치료", "정기적인 신경학적 평가"]
    
    return {
        "family_coping_ability": np.random.choice(["높음", "중간", "낮음"]),
        "environment_setting": np.random.choice(environments),
        "transfer_plan": np.random.choice(["ICU로 이송", "일반 병실로 이송", "수술실로 이송", "응급실로 이송"]),
        "followup_plan": np.random.choice(followup_plans),
        "nursing_record": np.random.choice(["환자 상태 기록", "간호 기록 없음"]),
        "nursing_evaluation": np.random.choice(["치료 후 상태 평가", "평가 없음"]),
        "multidisciplinary_collaboration": np.random.choice(["신경과 협진 필요", "없음"])
    }
