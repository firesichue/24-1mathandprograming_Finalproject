import numpy as np

def generate_patient_education():
    education_contents = [
        "뇌졸중 예방 및 관리",
        "뇌종양 치료 과정",
        "뇌출혈 후 회복",
        "외상성 뇌손상 관리",
        "뇌수막염 예방 및 치료"
    ]
    ethical_issues = [
        "응급 상황에서의 동의서",
        "의사결정 능력 제한 시 가족 동의",
        "환자의 사전 동의 없이 치료"
    ]
    
    return {
        "education_content": np.random.choice(education_contents),
        "ethical_issues": np.random.choice(ethical_issues)
    }
