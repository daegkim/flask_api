from flask import Flask, render_template, request
from database import db
from faceRecog import my_face_recog
import numpy as np
import json
import cv2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/vehicle', methods=['POST'])
def vehicle():
    data = request.data
    jsonstring = data.decode('utf-8')
    dict = json.loads(jsonstring)

    #try, fianlly를 사용하여 db에 오류가 생겨도 연결을 반드시 끊을 수 있도록 한다.
    try:
        my_db = db.db('test')
        my_db.db_connection()
        my_db.setVehicle(dict['number'])
    finally:
        my_db.db_end()

    #사실상 return할 필요가 없지만 flask에서는 view를 반드시 return 하도록 설정되어있다.
    return 'done'

@app.route('/human', methods=['POST'])
def human():
    data = request.data
    bytes_to_jpg = np.frombuffer(data, np.uint8)
    jpg_to_numpy = cv2.imdecode(bytes_to_jpg, 1)

    faceRecog = my_face_recog.FaceRecog()
    find = faceRecog.get_frame(jpg_to_numpy)

    cv2.imshow("test",find)
    while True:
        k=cv2.waitKey(0) & 0xFF
        if k==27:
            cv2.destroyAllWindows()
            break

    return 'done'

if __name__ == '__main__':
    app.run(debug = True)
