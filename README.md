# flask_api

※ cmd창 실행을 기준으로 작성하였습니다.

※ 개발환경(env)
    window 10 / 64bit
    python 3.6.5
    MariaDB 10.3

※ 라이브러리 설치(install lib)
    전부 다 [conda install ~]로 설치
    flask / pymysql / requests

1. 패키지를 참조할 수 있도록 해당 패키지의 경로를 아래와 같이 입력합니다.
    [set PYTHONPATH=C:/Users]
2. python route.py : 실행하면 flask서버가 실행됩니다.
3. postman을 활용하여 POST해볼 수 있습니다.
4. test/client.py를 활용하여 client쪽에서 명령을 보내는 것을 실행해볼 수 있습니다.

2018.10.31
# face_recognition 기능 추가

※ 윈도우에서 face_recognition 사용방법

0. python 3.6이 기본인 가상환경 생성
    - conda create --name faceRecog python=3.6

1. opencv 설치
    - python 3.6버전이 유지되어야 함
    - conda install -c conda-forge opencv를 사용하면 python3.6버전 유지하면서 설치 가능
    - 기타 방법이 안되는 이유
        ※ conda install -c menpo opencv : python 3.5로 downgrade 됨
        ※ pip install opencv-python : import가 되지 않음
        ※ 즉, python 3.6에서 돌아가는 opencv만 설치하면 됨

2. dlib설치
    - cmake설치해야 한다는 등의 오류 발생
    - https://pypi.python.org/simple/dlib에서 dlib-19.8.1-cp36-cp36m-win_amd64.whl을 다운로드
    - 다운로드 받은 .whl을 설치할 가상환경 폴더 밑에 복사
       ex)  C://Users/4/AppData/Local/conda/conda/envs/flask에 복사
              (다른 .whl파일들을 확인할 수 있음) 
              (숨김파일 볼 수 있도록 해야 AppData접근 가능)
    - 그 후 pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl로 설치
    - 기타 사항
        ※ .whl의 이름을 보면 cp36이 존재 -> 이는 python 3.6에서 설치가능하다는 것을 의미 -> 이 때문에 python 3.6필요

3. 나머지 모듈 설치
    - pip install face_recognition

4. 코드 다운로드
    - https://ukayzm.github.io/assets/face_recognition.zip에서 설치

5. 코드 관련
    - camera.py는 단순히 카메라 켜는 역할.
    - face_recog.py는 영상을 받아와서 얼굴이 있는지 폴더에 있는 사진과 비교
    - face_recog.py를 수정하여 영상이 아닌 frame을 받아와서 사진과 있는지 여부를 출력하도록 수정 필요
