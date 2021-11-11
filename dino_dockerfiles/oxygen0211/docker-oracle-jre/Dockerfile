FROM ubuntu:xenial
MAINTAINER Julian Engelhardt <jengelhardt211@gmail.com>


RUN apt-get update &&\
    apt-get install -y wget

RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/jre-8u172-linux-x64.tar.gz -c -O /tmp/jre.tar.gz &&\
    mkdir -p /opt/jre &&\
    tar --strip-components=1 -zxf /tmp/jre.tar.gz -C /opt/jre

RUN update-alternatives --install "/usr/bin/java" "java" "/opt/jre/bin/java" 1 &&\
    update-alternatives --install "/usr/bin/javaws" "javaws" "/opt/jre/bin/javaws" 1 &&\
    echo export JAVA_HOME=/opt/jre/ >> ~/.bashrc

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

CMD ["java", "-version"]
