from kafka import KafkaProducer 
value=input("Enter a value to be sent:")
print(value)
topic_name="nestDigital"
server="localhost:9092"
producer = KafkaProducer(bootstrap_servers = [server])
producer=KafkaProducer()
message=producer.send(topic_name, bytes(value,encoding='utf-8'))
metadata = message.get()
print(metadata.topic)
print(metadata.partition)