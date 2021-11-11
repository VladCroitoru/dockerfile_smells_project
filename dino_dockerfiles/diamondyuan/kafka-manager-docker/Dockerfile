FROM hseeberger/scala-sbt
MAINTAINER DiamondYuan <541832074@qq.com>

ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64 \
    KM_VERSION=1.3.3.13

RUN mkdir -p /tmp && \
    cd /tmp && \
    git clone https://github.com/yahoo/kafka-manager && \
    cd /tmp/kafka-manager && \
    git checkout ${KM_VERSION}

WORKDIR /tmp/kafka-manager
RUN /bin/echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt
RUN sbt clean dist && \
    unzip  -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \
    rm -fr /tmp/*

EXPOSE 9000
WORKDIR /kafka-manager-${KM_VERSION}
ENTRYPOINT ["./bin/kafka-manager","-Dconfig.file=conf/application.conf"]