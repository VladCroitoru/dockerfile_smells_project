FROM openjdk:latest

RUN apt-get update && \
    apt-get install curl \
                    wget \
                    vim \
                    apt-transport-https \
                    sudo \
                    netcat \
                    iputils-ping \
                    net-tools \
                    vifm \
                    libx11-6 \
                    tcpdump \
                    hexedit -y --no-install-recommends \
    && mkdir /logstash/ && wget https://artifacts.elastic.co/downloads/logstash/logstash-6.1.1.tar.gz \
    && tar -xzf logstash-6.1.1.tar.gz -C /logstash/ && rm logstash-6.1.1.tar.gz

WORKDIR /logstash/
