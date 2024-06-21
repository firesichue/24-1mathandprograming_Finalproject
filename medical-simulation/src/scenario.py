import numpy as np

def generate_scenario():
    scenario_types = ["뇌졸중", "뇌종양", "뇌출혈", "외상성 뇌손상", "뇌수막염"]
    emergency_settings = ["의식 저하", "발작", "급성 마비", "급성 두통", "급성 시력 저하"]
    treatment_goals = ["뇌압 감소", "출혈 억제", "신경 보호", "종양 제거", "감염 치료"]
    medications = ["만니톨", "파라세타몰", "다이아제팜", "페니토인", "세프타지딤"]
    nursing_interventions = ["산소 공급", "IV 라인 확보", "신경학적 상태 모니터링", "심폐소생술 준비", "항생제 투여"]
    
    return {
        "scenario_type": np.random.choice(scenario_types),
        "emergency_setting": np.random.choice(emergency_settings),
        "treatment_goal": np.random.choice(treatment_goals),
        "medication_and_dosage": np.random.choice(medications),
        "nursing_intervention": np.random.choice(nursing_interventions)
    }
