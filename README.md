# 24-1mathandprograming_Finalproject

" 가상 환자 시뮬레이션 실습 : 환자 케이스 자동생성 프로그램 (신경계 환자ver)

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
    - 국가건강정보포털
    - 대한민국 정책브리핑 
    - 국가암정보센터 
    - 국립중앙의료원 
    - 등 노인 발병률 등 Real world와 정합성 위해 레퍼런스 내 구체적 수치 참고함
      ( 뇌혈관질환 환자 수는 '18년 96만 7,311명 대비 '22년 117만 1,534명으로 21.1%(연평균 4.9%) 증가했고, 뇌졸중 환자 수는 '18년 59만 1,946명 대비 '22년 63만 4,177명으로 7.1%(연평균 1.7%) 증가했다)
    - 위와같은 수치 참고하여 코딩
 
4. 모델 개요 설명 ( Readme 문서 마지막에 코드 설명)
    - 기본적 정보 (키, 몸무게, 혈압, 심박수) 등의 상관관계 고려하여 범위 설정 하였음.
    - 정규 분포 등 수학적/통계적 도구 적용함
    - generate_full_scenario (메인함수) 실행시 다음과 같은 케이스 등장함
    - 
     ![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/982c9971-e64d-44bf-8e08-0bf84f8abbf7)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/756ebabe-a0bb-4043-8839-f6ca8acfa20a)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/8a9dd8f4-68dd-497f-915d-ce1834e48324)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/b8525985-cc2e-497b-8765-85212b850877)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/2249c131-f26d-4592-9629-646c8aa066d2)

    

5. 실효성, 타당성 확인
    - 도메인 전문가(간호대학 교수)의  실효성 인증. 추후 세브란스 디지털헬스케어 센터 인턴으로 교육프로그램 개발 권유 받음.
    - 테스트 디렉토리를 통하여 케이스 수치에 신뢰도 보장함.
    
6. 추후 보완책
    1. UI 구축으로 프로그램의 제품화 고려
    2. 단순 케이스 제시를 넘어서, 해결 해야하는 문제를 케이스마다 다르게 임의로 제시하는 등 프로그램의 완결성 확보 
    3. chat gpt API를 통해,  data set을 chat gpt에 입력하여 환자와 대화할 수 있는 대화적 요소 추가 고려


  
# 주요 코드 설명

requirements는 numpy 위주로. 간단하게 구축 
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/51bb47dc-5aa5-49f2-ae38-fd6b41fd4356)


Main 함수에서 Full scenario 를 return 하도록
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/b9ec3f4f-a056-40e9-a4d8-53fc34b599b1)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/dfd1ff9f-fa4d-4151-ada9-7e7450fa4522)


real world 근거 기반하여 디테일하게 generating 범위 설정함
몸무게, 신장, 성별, 혈압, 심박수 간의 종속성 부여함
정규분포 적용함
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/b1711ad9-c9b4-45ec-a676-91f691ff60a8)


환자의 history 역시 동일 확률분포가 아닌 real world 근거 기반하였으나, 0.05 단위로 거칠게 범위 설정함.
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/67a10461-52f1-4f66-a6b1-49537eafeff9)

프로그램의 완성도를 위해 시나리오에서 고려 가능한 거의 모든 부분의 parameter를 기획, 구성함

# Patient Information (환자 정보)
이름 (name): 환자의 이름  
나이 (age): 환자의 나이  
성별 (gender): 환자의 성별 (남성/여성)  
키 (height): 환자의 키 (cm)  
몸무게 (weight): 환자의 몸무게 (kg)  
혈압 (blood_pressure): 환자의 혈압 (mmHg)  
수축기 혈압 (systolic BP)  
이완기 혈압 (diastolic BP)  
심박수 (heart_rate): 환자의 심박수 (bpm)  
호흡수 (respiratory_rate): 환자의 호흡수 (breaths/min)  
체온 (temperature): 환자의 체온 (°C)  
산소 포화도 (oxygen_saturation): 환자의 산소 포화도 (%)  
혈당 (blood_sugar): 환자의 혈당 (mg/dL)  

# Medical History (의료 기록)
병력 (medical_history): 환자가 앓고 있는 질병 목록 (예: 고혈압, 고지혈증)  
현재 복용 약물 (current_medications): 환자가 현재 복용 중인 약물 목록 (예: 아스피린, 리피토)  
알레르기 (allergies): 환자가 가지고 있는 알레르기 (예: 없음)  
주요 증상 (primary_symptom): 환자가 주로 호소하는 증상 (예: 두통)  
부차적 증상 (secondary_symptoms): 환자가 부수적으로 호소하는 증상 (예: 어지럼증, 구토)  
신체 검사 (physical_examination): 신체 검사 결과 (예: 신경학적 이상 소견)  
진단 결과 (diagnostic_results): 진단 결과 요약 (예: CT: 뇌출혈 확인)  
전자 건강 기록 (EHR): 환자의 전자 건강 기록 여부 (예: 있음)  

# Diagnostic Results (진단 결과)
CT 결과 (CT_result): CT 검사 결과 (예: 뇌출혈 확인)  
MRI 결과 (MRI_result): MRI 검사 결과 (예: 정상)  
신경학적 검사 (neurological_exam): 신경학적 검사 결과 (예: 좌측 편마비)  
EEG 결과 (EEG_result): 뇌파 검사 결과 (예: 정상)  
CSF 분석 (CSF_analysis): 뇌척수액 분석 결과 (예: 정상)  

# Additional Information (추가 정보)
가족력 (family_history): 가족 질병 역사 (예: 부모님 고혈압)  
생활습관 (lifestyle): 환자의 생활습관 (예: 비흡연, 음주 가끔)  
GCS (GCS): 글래스고 코마 스케일 (점수) (예: 13)  
통증 점수 (pain_score): 환자가 느끼는 통증의 정도 (0-10점) (예: 6)  
환자 협조도 (patient_cooperation): 환자의 협조도 (예: 중간)  
감정 상태 (emotional_state): 환자의 감정 상태 (예: 불안)  
피부 상태 (skin_condition): 환자의 피부 상태 (예: 정상)  

# Scenario (시나리오)
시나리오 유형 (scenario_type): 시나리오의 유형 (예: 뇌출혈)  
응급 상황 설정 (emergency_setting): 응급 상황의 설정 (예: 의식 저하)  
치료 목표 (treatment_goal): 치료의 주요 목표 (예: 출혈 억제)  
약물 및 용량 (medication_and_dosage): 처방된 약물 및 용량 (예: 만니톨)  
간호 중재 (nursing_intervention): 필요한 간호 중재 (예: 산소 공급)  

# Patient Education (환자 교육)
교육 내용 (education_content): 환자에게 제공되는 교육 내용 (예: 뇌출혈 후 회복)  
윤리적 문제 (ethical_issues): 윤리적 문제 (예: 의사결정 능력 제한 시 가족 동의)  

# Environment and Followup (환경 및 추적 계획)
가족의 대처 능력 (family_coping_ability): 가족의 대처 능력 (예: 중간)  
환경 설정 (environment_setting): 환자의 환경 설정 (예: ICU)  
이송 계획 (transfer_plan): 환자의 이송 계획 (예: ICU로 이송)  
추적 계획 (followup_plan): 환자의 추적 계획 (예: 신경과 협진)  
간호 기록 (nursing_record): 간호 기록 여부 (예: 환자 상태 기록)  
간호 평가 (nursing_evaluation): 간호 평가 여부 (예: 치료 후 상태 평가)  
다학제 협업 (multidisciplinary_collaboration): 다학제 협업 필요 여부 (예: 신경과 협진 필요)  
