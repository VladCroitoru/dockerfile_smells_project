FROM java:8
MAINTAINER Nicholas Johns <nicholas.a.johns5@gmail.com>

ENV KAFKA_VERSION=2.3.0
ENV KAFKA_URL=http://mirrors.sonic.net/apache/kafka/${KAFKA_VERSION}/kafka_2.12-${KAFKA_VERSION}.tgz
ENV KAFKA_TMP_DEST=/opt/kafka.tgz
ENV KAFKA_WORKDIR=/opt/kafka

ADD run.sh /opt/run.sh

RUN chmod +x /opt/run.sh && \
    wget $KAFKA_URL -O ${KAFKA_TMP_DEST} && \
    mkdir -p ${KAFKA_WORKDIR} && \
    tar -xvzpf ${KAFKA_TMP_DEST} --strip-components=1 -C ${KAFKA_WORKDIR}

WORKDIR [ "/opt" ]
ENTRYPOINT [ "/opt/run.sh" ]
