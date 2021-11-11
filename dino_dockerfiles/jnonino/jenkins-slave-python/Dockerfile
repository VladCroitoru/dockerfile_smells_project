FROM python:alpine
LABEL maintainer="CN Services <noninojulian@gmail.com>"

ENV JAVA_VERSION 8u212
ENV JAVA_ALPINE_VERSION 8.212.04-r0

RUN apk add --no-cache  && \
    apk add --no-cache git subversion mercurial wget curl unzip openssh ca-certificates procps bash openjdk8 && \
    rm -rf /var/cache/apk/*

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $JAVA_HOME/bin:$JAVA_HOME/lib:$PATH

RUN addgroup -S -g 10000 jenkins && \
    adduser -S -u 10000 -h /home/jenkins -G jenkins jenkins

USER jenkins
WORKDIR /home/jenkins

CMD ["/bin/sh"]
