from flask import Flask, render_template, request
from database import db
import json


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

if __name__ == '__main__':
    app.run(debug = True)
