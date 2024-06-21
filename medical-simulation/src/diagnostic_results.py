import numpy as np

def generate_diagnostic_results():
    return {
        "CT_result": np.random.choice(["뇌출혈 확인", "경미한 출혈", "정상"]),
        "MRI_result": np.random.choice(["미세 뇌경색 소견", "뇌종양 발견", "정상"]),
        "neurological_exam": np.random.choice(["좌측 편마비", "우측 편마비", "정상"]),
        "EEG_result": np.random.choice(["발작 소견", "정상"]),
        "CSF_analysis": np.random.choice(["정상", "백혈구 증가", "단백질 증가", "감염 의심"])
    }
