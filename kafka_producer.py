import time
import json
from kafka.producer import KafkaProducer
import requests

kafka_boostrap_servers = '127.0.0.1:9092'
kafka_topic_name = 'temperaturas'

producer = KafkaProducer(bootstrap_servers=kafka_boostrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))
json_message = None
nome_cidade = None
temperatura = None
umidade = None
openweathermap_api_endpoint = None
appid = None


def get_weather_detail(openweathermap_api_endpoint):
    api_response = requests.get(openweathermap_api_endpoint)
    json_data = api_response.json()
    nome_cidade = json_data['name']
    umidade = json_data['main']['humidity']
    temperatura = json_data['main']['temp']
    temperatura = float(temperatura) - 273.15
    temperatura = float("{:.2f}".format(temperatura))
    json_message = {'NomeCidade': nome_cidade, 'Temperatura': temperatura, 'Umidade': umidade,
                    'CreationTime': time.strftime('%Y-%m%d %H:%M:%S')}
    return json_message


def get_appid(appid):
    if appid is None:
        appid = "78f12d31ea56f9fff2c792c49ad29909"
    else:
        pass
    return appid


while True:
    nome_cidade = 'São Paulo'
    appid = get_appid(appid)
    openweathermap_api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?q=' + nome_cidade + '&APPID=' + appid
    json_message = get_weather_detail(openweathermap_api_endpoint)
    producer.send(kafka_topic_name, json_message)
    print("Published Message 1:" + json.dumps(json_message))
    print("Wait for 2 seconds... ")
    time.sleep(2)

    nome_cidade = 'Rio de Janeiro'
    appid = get_appid(appid)
    openweathermap_api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?q=' + nome_cidade + '&APPID=' + appid
    json_message = get_weather_detail(openweathermap_api_endpoint)
    producer.send(kafka_topic_name, json_message)
    print("Published Message 1:" + json.dumps(json_message))
    print("Wait for 2 seconds... ")
    time.sleep(2)

    nome_cidade = 'Brasília'
    appid = get_appid(appid)
    openweathermap_api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?q=' + nome_cidade + '&APPID=' + appid
    json_message = get_weather_detail(openweathermap_api_endpoint)
    producer.send(kafka_topic_name, json_message)
    print("Published Message 1:" + json.dumps(json_message))
    print("Wait for 2 seconds... ")
    time.sleep(2)
    
    time.sleep(120)