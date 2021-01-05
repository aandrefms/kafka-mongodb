from kafka.consumer import KafkaConsumer

kafka_boostrap_servers = '127.0.0.1:9092'
kafka_topic_name = 'cities'

consumer = KafkaConsumer('cities', bootstrap_servers=kafka_boostrap_servers,
                         auto_offset_reset='earliest', enable_auto_commit=False)
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print (message.value.decode('utf-8'))