FROM openjdk:8-jdk-alpine
ENV SBT_VERSION  0.13.15
ENV SBT_HOME /usr/local/sbt
ENV PATH=${PATH}:${SBT_HOME}/bin
ENV SBT_JAR http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz

RUN apk --update add bash wget curl tar git && \
    wget ${SBT_JAR} -O sbt-$SBT_VERSION.tgz -o /dev/null && \
    tar -xf sbt-$SBT_VERSION.tgz -C /usr/local && \
    echo -ne "- with sbt sbt-$SBT_VERSION\n" >> /root/.built && \
    rm sbt-$SBT_VERSION.tgz && \
    sbt sbt-version && \
    apk del wget tar && \
    rm -rf /var/cache/apk/*

CMD ["/bin/bash"]
