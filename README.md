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
     ![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/982c9971-e64d-44bf-8e08-0bf84f8abbf7)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/756ebabe-a0bb-4043-8839-f6ca8acfa20a)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/8a9dd8f4-68dd-497f-915d-ce1834e48324)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/b8525985-cc2e-497b-8765-85212b850877)
![image](https://github.com/firesichue/24-1mathandprograming_Finalproject/assets/170858202/2249c131-f26d-4592-9629-646c8aa066d2)

    

1. 실효성, 타당성 확인
    - 도메인 전문가(간호대학 교수)의  실효성 인증. 추후 세브란스 디지털헬스케어 센터 인턴으로 교육프로그램 개발 권유 받음.
    - 테스트 디렉토리를 통하여 케이스 수치에 신뢰도 보장함.
    
2. 추후 보완책
    1. UI 구축으로 프로그램의 제품화 고려
    2. 단순 케이스 제시를 넘어서, 해결 해야하는 문제를 케이스마다 다르게 임의로 제시하는 등 프로그램의 완결성 확보 
    3. chat gpt API를 통해,  data set을 chat gpt에 입력하여 환자와 대화할 수 있는 대화적 요소 추가 고려
