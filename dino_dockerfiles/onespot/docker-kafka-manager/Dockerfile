FROM hseeberger/scala-sbt:8u141-jdk_2.12.3_1.0.1

ARG KM_VERSION

MAINTAINER Richard Bolkey <rick@onespot.com>

RUN mkdir -p /tmp && \
    cd /tmp && \
    wget https://github.com/yahoo/kafka-manager/archive/${KM_VERSION}.tar.gz && \
    tar xxf ${KM_VERSION}.tar.gz && \
    cd /tmp/kafka-manager-${KM_VERSION} && \
    sbt clean dist && \
    unzip  -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \
    rm -fr /tmp/${KM_VERSION} /tmp/kafka-manager-${KM_VERSION} && \
    mkdir /conf && \
    cp /kafka-manager-${KM_VERSION}/conf/application.conf /conf/application.conf

WORKDIR /kafka-manager-${KM_VERSION}

VOLUME ["/conf"]

EXPOSE 9000
ENTRYPOINT ["./bin/kafka-manager","-Dconfig.file=/conf/application.conf"]
