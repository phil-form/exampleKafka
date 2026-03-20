from kafka import KafkaProducer
kafka_url = 'localhost:9092'
producer = KafkaProducer(
    bootstrap_servers=kafka_url,
    value_serializer=lambda v: str(v).encode('utf-8')
)

person_topic='persons'
with open('data/test.csv') as file:
    lines = file.readlines()
    for line in lines:
        producer.send(person_topic, value=line.strip().encode('utf-8'))

    producer.flush()
    producer.close()