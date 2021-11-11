FROM openjdk:8-alpine
MAINTAINER "冯宇<yu.feng@shifudao.com>"

ENV GRADLE_VERSION 3.1
RUN apk update && apk add openssl bash libstdc++ && rm -fr /var/cache/apk/*
RUN cd /usr/share && \
    wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip && \
    unzip gradle-${GRADLE_VERSION}-bin.zip && \
    rm -f gradle-${GRADLE_VERSION}-bin.zip
RUN ln -s /usr/share/gradle-${GRADLE_VERSION}/bin/gradle /usr/bin/
RUN mkdir -p /usr/src/

WORKDIR /usr/src/

CMD ["gradle"]
