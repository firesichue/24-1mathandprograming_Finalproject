# 24-1mathandprograming_Finalproject


1. 동기 (프로그램 관점)
    1. 본인은 연세대학교 간호대학 간호학과 주 전공 학생으로, 여러차례 가상 환자 시뮬레이션 실습을 진행한 바 있음.
    2. 수학과의 퀴즈시험과도 같은 상당한 배점의 실습이지만 매년 동일 주제에 대해 거의 동일한 환자 케이스를 가정함
    3. 게다가, 같은 과목 수강생에게도 동일한 가상환자 케이스를 제시함. 따라서 앞선 실습 학생의 정보 유출 등으로 형평성 이슈 생김
    4. 또한 가상 환자 시뮬레이션을 수학 예제문제 풀 듯 경험 할 수 있는 프로그램이 없음. 고정된 환자 케이스를 학습할 수 있는 프로그램은 있으나 무작위로 환자를 가정하는 프로그램의 부재
    5. Chat-gpt 등의 무작위 생성으로는 국내의 homogenous한 인구 분포에 적합하지 않은 케이스를 제시함. 예컨데 해외에서는 인종별 발병률이 극심히 차이나는 질병에 대해  매우 강조. 국내에서는 거의 강조 안함. 

2. 동기 (수업 관점)
    1. 수업에서 학습한 numpy 등을 사용. rule based로 코딩함
    2. 테스트 디렉토리를 추가 생성하여 추후 변경에 대한 (치료 지침의 변화 등) 리펙토리 지원 및 신뢰성 향상 
    
3. 데이터 셋 :
    - 국가건강정보포털 (http://health.kdca.go.kr/healthinfo/biz/health/childhood/view.do?cntno=97&menu_no=2220)
    - 대한민국 정책브리핑 (http://www.korea.kr/news/policyNewsView.do?newsId=148889016)
    - 국가암정보센터 (http://www.cancer.go.kr/lay1/program/S1T211C221/cancer/view.do?cancer_seq=2776)
    - 국립중앙의료원 (http://www.nmc.or.kr/medical/treatment/view.do?tmIndex=79)
    - 등 노인 발병률 등 Real world와 정합성 위해 레퍼런스 내 구체적 수치 참고함 ( 연령대별 발병 비율 등)

1. 모델 설명
    - 기본적 정보 (키, 몸무게, 혈압, 심박수) 등의 상관관계 고려하여 범위 설정 하였음.
    - 정규 분포 등 수학적/통계적 도구 적용함
    - generate_full_scenario (메인함수) 실행시 다음과 같은 케이스 등장함
    - 
    
    {
    "Patient Information": {
    "name": "안재근",
    "age": 60,
    "gender": "남성",
    "height": 178,
    "weight": 101,
    "blood_pressure": "138/84 mmHg",
    "heart_rate": "76 bpm",
    "respiratory_rate": "19 breaths/min",
    "temperature": "37.2°C",
    "oxygen_saturation": "94%",
    "blood_sugar": "123 mg/dL"
    },
    "Medical History": {
    "medical_history": [
    "고혈압",
    "고지혈증"
    ],
    "current_medications": [
    "아스피린",
    "리피토"
    ],
    "allergies": "없음",
    "primary_symptom": "두통",
    "secondary_symptoms": [
    "어지럼증",
    "구토"
    ],
    "physical_examination": "신경학적 이상 소견",
    "diagnostic_results": "CT: 뇌출혈 확인",
    "EHR": "전자 건강 기록 있음"
    },
    "Diagnostic Results": {
    "CT_result": "뇌출혈 확인",
    "MRI_result": "정상",
    "neurological_exam": "좌측 편마비",
    "EEG_result": "정상",
    "CSF_analysis": "정상"
    },
    "Additional Information": {
    "family_history": "부모님 고혈압",
    "lifestyle": "비흡연, 음주 가끔",
    "GCS": 13,
    "pain_score": 6,
    "patient_cooperation": "중간",
    "emotional_state": "불안",
    "skin_condition": "정상"
    },
    "Scenario": {
    "scenario_type": "뇌출혈",
    "emergency_setting": "의식 저하",
    "treatment_goal": "출혈 억제",
    "medication_and_dosage": "만니톨",
    "nursing_intervention": "산소 공급"
    },
    "Patient Education": {
    "education_content": "뇌출혈 후 회복",
    "ethical_issues": "의사결정 능력 제한 시 가족 동의"
    },
    "Environment and Followup": {
    "family_coping_ability": "중간",
    "environment_setting": "ICU",
    "transfer_plan": "ICU로 이송",
    "followup_plan": "신경과 협진",
    "nursing_record": "환자 상태 기록",
    "nursing_evaluation": "치료 후 상태 평가",
    "multidisciplinary_collaboration": "신경과 협진 필요"
    }
    }
    

1. 실효성, 타당성 확인
    - 도메인 전문가(간호대학 교수)의  실효성 인증. 추후 세브란스 디지털헬스케어 센터 인턴으로 교육프로그램 개발 권유 받음.
    - 테스트 디렉토리를 통하여 케이스 수치에 신뢰도 보장함.
    
2. 추후 보완책
    1. UI 구축으로 프로그램의 제품화 고려
    2. 단순 케이스 제시를 넘어서, 해결 해야하는 문제를 케이스마다 다르게 임의로 제시하는 등 프로그램의 완결성 확보 
    3. chat gpt API를 통해,  data set을 chat gpt에 입력하여 환자와 대화할 수 있는 요소 추가 고려
