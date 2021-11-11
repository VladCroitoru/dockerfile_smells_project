FROM ubuntu:20.04

ENV CORRETTO_URL=https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.deb
ENV CORRETTO_PACKAGE=amazon-corretto-11-x64-linux-jdk.deb
ENV KAFKA_URL=https://dlcdn.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
ENV KAFKA_PACKAGE=kafka_2.13-2.8.0.tgz
ENV KAFKA_VERSION=kafka_2.13-2.8.0

RUN cd /root \
    && apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install curl ansible java-common vim \
    && curl -OfsSL ${CORRETTO_URL} \
    && dpkg --install ~/${CORRETTO_PACKAGE} \
    && curl -OfsSL ${KAFKA_URL} \
    && tar -C /usr/local/ -xvf ~/${KAFKA_PACKAGE} \
    && ln -s /usr/local/${KAFKA_VERSION} /usr/local/kafka  \
    && rm /root/${KAFKA_PACKAGE} \
    && rm /root/${CORRETTO_PACKAGE} \
    && echo 'export PATH=${PATH}:/usr/local/kafka/bin' >> ~/.bashrc

COPY entrypoint.sh /

RUN chmod 755 /entrypoint.sh

CMD ["bash", "/entrypoint.sh"]
