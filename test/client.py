import requests, json
import models


#init
url='http://127.0.0.1:5000/vehicle'
headers = {'Content-Type': 'application/json; charset=utf-8'}

#값을 입력받아서 class에 저장
my_vehicle = models.vehicle_info()
data = input("car number : ")
my_vehicle.setNumber(data)

#class자체를 jsonstring으로 바꿔준다.
my_json = my_vehicle.toJSON()

#이 데이터를 가지고 server에 POST요청한다.
response = requests.post(url, data=my_json)

#만약 잘 받았다면 상태코드가 200으로 올 것이다.
if response.status_code == 200:
    print('ok')
