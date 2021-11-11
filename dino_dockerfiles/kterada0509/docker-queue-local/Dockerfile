FROM openjdk:13-alpine

RUN set -x \
    && apk update \
    && apk add python3 curl \
    && curl https://bootstrap.pypa.io/get-pip.py | python3 \
    && pip install awscli \
    && rm -rf /var/cache/apk/*

ENV ELASTICMQ_SERVER_VERSION=0.14.6

ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-${ELASTICMQ_SERVER_VERSION}.jar /elasticmq-server.jar
ENTRYPOINT ["/opt/openjdk-13/bin/java", "-jar", "/elasticmq-server.jar"]

EXPOSE 9324

CMD ["-help"]
