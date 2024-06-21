import numpy as np
from utils import weighted_choice

def generate_patient_info():
    names = ["안재근", "안재순", "안재훈", "안재은", "안재현", "안재연", "안재인"]
    ages = [(20, 0.05), (25, 0.05), (35, 0.1), (45, 0.1), (50, 0.2), (60, 0.2), (70, 0.15), (80, 0.15)]
    genders = [("남성", 0.5), ("여성", 0.5)]

    name = np.random.choice(names)
    age = weighted_choice(ages)
    gender = weighted_choice(genders)

    # 성별에 따라 키 결정 (남성은 평균적으로 더 큼)
    if gender == "남성":
        height = np.random.normal(175, 10)
    else:
        height = np.random.normal(165, 10)

    height = max(150, min(190, int(height)))  # 키를 150cm에서 190cm 사이로 제한

    # 키에 기반하여 몸무게 결정 (단순화된 BMI 관련 계산)
    weight = height - 100 + np.random.normal(0, 10)
    weight = max(100, int(weight))  # 몸무게를 100kg 이상으로 제한

    # 신경계 질환 주제에 초점 맞추기 위해, 몸무게 100kg, 심박수 130 등 보수적으로 범위를 잡음.

    # 몸무게에 따라 혈압 결정하도록. evidnce에 따라 종속 관계를추가했음 
    systolic_bp = 90 + (weight - 50) * 0.5 + np.random.normal(0, 10)
    diastolic_bp = 60 + (weight - 50) * 0.3 + np.random.normal(0, 5)
    blood_pressure = f"{int(systolic_bp)}/{int(diastolic_bp)} mmHg"

    # 심박수 결정
    heart_rate = 70 + np.random.normal(0, 15)
    heart_rate = max(50, min(130, int(heart_rate)))  # 심박수를 50에서 130 bpm 사이로 제한

    # 몸무게에 따라 혈당 결정.  
    blood_sugar = 80 + (weight - 50) * 0.5 + np.random.normal(0, 30)
    blood_sugar = max(60, min(400, int(blood_sugar)))  # 혈당을 60에서 400 mg/dL 사이로 제한

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "blood_pressure": blood_pressure,
        "heart_rate": f"{heart_rate} bpm",
        "respiratory_rate": f"{np.random.randint(10, 30)} breaths/min",
        "temperature": f"{np.random.uniform(35.0, 39.0):.1f}°C",
        "oxygen_saturation": f"{np.random.randint(85, 100)}%",
        "blood_sugar": f"{blood_sugar} mg/dL"
    }
