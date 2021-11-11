FROM progrium/busybox
MAINTAINER Matthias Hryniszak <padcom@gmail.com>

RUN opkg-install curl

RUN mkdir -p /usr/lib/jvm && \
    curl -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/server-jre-8u121-linux-x64.tar.gz -L -k | gzip -dc | tar -xf - -C /usr/lib/jvm && \
    ln -s /usr/lib/jvm/jdk1.8.0_121 /usr/lib/jvm/default-java && \
    ln -s /usr/lib/jvm/default-java/bin/java /usr/bin/java

ENV JAVA_HOME /usr/lib/jvm/default-java
