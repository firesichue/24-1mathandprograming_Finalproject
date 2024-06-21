import numpy as np

def generate_medical_history():
    histories = [("고혈압", 0.3), ("당뇨병", 0.2), ("고지혈증", 0.2), ("심장병", 0.1), ("신장병", 0.05), ("천식", 0.05), ("간질", 0.1)] # 상관관계에 따라 확률 차등부여
    current_medications = ["아스피린", "메트포르민", "아테놀롤", "리피토", "와파린", "알부테롤", "페니토인"]
    allergies = ["페니실린", "없음", "설파제", "아스피린", "조개류", "꽃가루"] #임의로 설정. 과거력 측정 여부 확인위해. ㅇ
    
    return {
        "medical_history": np.random.choice(histories, size=np.random.randint(1, 5), replace=False).tolist(),
        "current_medications": np.random.choice(current_medications, size=np.random.randint(1, 5), replace=False).toligst(),
        "allergies": np.random.choice(allergies),
        "primary_symptom": np.random.choice(["두통", "마비", "어지럼증", "시력 저하"]),
        "secondary_symptoms": np.random.choice(["구토", "시야 장애", "청력 감소", "발작", "언어 장애"], size=np.random.randint(0, 4), replace=False).tolist(),
        "physical_examination": np.random.choice(["신경학적 이상 소견", "정상", "반사 이상"]),
        "diagnostic_results": np.random.choice(["CT: 뇌출혈 확인", "MRI: 뇌종양 발견", "EEG: 발작 소견", "정상"]),
        "EHR": np.random.choice(["전자 건강 기록 있음", "없음"])
    }
