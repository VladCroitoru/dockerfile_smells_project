FROM ubuntu:precise
ADD https://github.com/bowlofstew/http-to-kafka/releases/download/1.0-alpha/http-to-kafka /kafka_http/
ADD src/config.json /kafka_http/
WORKDIR /kafka_http/
CMD http-to-kafka config.json 
