import numpy as np

def generate_additional_info():
    return {
        "family_history": np.random.choice(["부모님 고혈압", "없음", "부모님 당뇨병", "부모님 심장병"]),
        "lifestyle": np.random.choice(["비흡연, 음주 가끔", "흡연, 음주 잦음", "비흡연, 음주 없음"]),
        "GCS": np.random.randint(3, 16),
        "pain_score": np.random.randint(0, 11),
        "patient_cooperation": np.random.choice(["높음", "중간", "낮음"]),
        "emotional_state": np.random.choice(["불안", "평온", "혼란", "우울"]),
        "skin_condition": np.random.choice(["정상", "발진", "상처", "멍"])
    }
