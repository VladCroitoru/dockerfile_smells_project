FROM debian:jessie
MAINTAINER Aditya Manthramurthy

RUN apt-get -q update && apt-get install -qy \
    openjdk-7-jre-headless wget python-minimal curl

RUN wget -q -O - http://apache.osuosl.org/kafka/0.8.2.1/kafka_2.10-0.8.2.1.tgz | tar -xzf - -C /opt \
    && mv /opt/kafka_2.10-0.8.2.1 /opt/kafka

EXPOSE 9092

VOLUME ["/kafka", "/var/log/kafka"]

ADD run.py /opt/kafka/.docker/run.py
RUN chmod +x /opt/kafka/.docker/run.py

ENTRYPOINT ["/opt/kafka/.docker/run.py"]
