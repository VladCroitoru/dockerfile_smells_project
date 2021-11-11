FROM alpine:3.4
    
RUN set -x && \
    apk add --no-cache \
      openjdk8 \
      openjdk7 \
      git \
      openssh-client \
      bash

COPY sbt-extras/sbt /bin/sbt
RUN chmod u+x /bin/sbt

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

VOLUME /root/.sbt /root/.ivy2 /root/project
WORKDIR /root/project

