FROM ubuntu:14.04 

RUN apt-get update && apt-get install -y openjdk-7-jre curl

ENV VERSION=1.8.2

RUN mkdir /opt/maxwell 
WORKDIR /opt/maxwell

RUN curl -sLo - https://github.com/zendesk/maxwell/releases/download/v${VERSION}/maxwell-${VERSION}.tar.gz | tar zxvf - \
      && mv maxwell-${VERSION} ${VERSION}

WORKDIR /opt/maxwell/${VERSION}

ENV MYSQL_USER=root
ENV MYSQL_HOST=127.0.0.1
ENV MYSQL_PORT=3306
ENV KAFKA_HOST=127.0.0.1
ENV KAFKA_PORT=9092
ENV KAFKA_VERSION=0.10
ENV KAFKA_TOPIC=maxwell
ENV LOG_LEVEL=WARN
ENV PRODUCER=kafka

CMD bin/maxwell --user=$MYSQL_USER --password=$MYSQL_PASSWORD --host=$MYSQL_HOST --port=$MYSQL_PORT --producer=$PRODUCER --kafka_version=$KAFKA_VERSION --kafka.bootstrap.servers=$KAFKA_HOST:$KAFKA_PORT --kafka_topic=$KAFKA_TOPIC --log_level=$LOG_LEVEL
