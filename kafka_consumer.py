from kafka.consumer import KafkaConsumer
import config_db
import ast

kafka_boostrap_servers = '127.0.0.1:9092'
kafka_topic_name = 'temperaturas'

consumer = KafkaConsumer(kafka_topic_name, bootstrap_servers=kafka_boostrap_servers,
                         auto_offset_reset='earliest', enable_auto_commit=False)  # earliest
for message in consumer:
    item = message.value.decode('utf-8')
    config_db.inserir_database(ast.literal_eval(item))
    print(message.value.decode('utf-8'))