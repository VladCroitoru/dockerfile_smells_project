FROM openjdk:latest

RUN cd /opt && curl -OL https://archive.apache.org/dist/kafka/2.8.0/kafka_2.13-2.8.0.tgz && tar -zxvf kafka_2.13-2.8.0.tgz && rm kafka_2.13-2.8.0.tgz

WORKDIR /opt/kafka_2.13-2.8.0/

COPY start-kafka.sh /opt/kafka_2.13-2.8.0/

RUN sed -i -e 's/\r$//' start-kafka.sh

RUN chmod 755 start-kafka.sh

CMD ["./start-kafka.sh"]