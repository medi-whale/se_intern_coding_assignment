# se_intern_coding_assignment

## 과제의 목적
    - 파일명(str) 을 적절하게 파싱
    - SQLITE 를 사용하기위한 sql 문 작성
    - requests 패키지를 사용한 API 요청 코드 작성

## 과제 수행
    - pip install -r requirments.txt 명령어를 사용해 본인의 환경 또는 제공한 환경에 필요한 python package 를 설치한다.
    - 제공되는 이미지를 images 폴더에 넣어 on_created 함수 실행되는 것을 확인
    - on_created 함수를 완성한다.

## 보충설명
    - watdog(https://pypi.org/project/watchdog/) 파일 감시 패키지로 images 폴더에 파일이 생성되면 on_created 함수가 실행된다.
    - 제공되는 이미지는 모두 <patient_id>_<exam_date>_<R/L>.jpg 형식의 파일명을 가지고 있다.
    - API 는 아래 예시처럼 데이터와 이미지 파일을 업로드 하는 식으로 요청한다. 
    """
    endpoint : https://test.mediwhale.ai/local_uploader/upload
    data
        file1 : 이미지 파일
        patient_id: <파일명에서 파싱>,
        exam_date: <파일명에서 파싱>,
        "member_id": "master",
        "member_pw": "default1234",
        "sex" : "M",
        "age": 60,
        "laterality" : <파일명에서 파싱>,
        "output_type":"encrypted_id"
    """

    - 파일명에서 얻을 수 있는 정보 빼고는 나머지는 그대로 올리셔도 됩니다.