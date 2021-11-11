FROM debian:buster
LABEL arch="arm|arm64"
ENV DEBIAN_FRONTEND=noninteractive

ARG tcversion=9.0.50
ARG jenkinsversion=2.301

ARG tomcat=https://downloads.apache.org/tomcat/tomcat-9/v$tcversion/bin/apache-tomcat-$tcversion.tar.gz
ARG jenkins=https://get.jenkins.io/war/$jenkinsversion/jenkins.war

ADD $tomcat .
ADD $jenkins .

RUN \
    apt update && \
    apt install -y \
      openjdk-11-jre-headless git && \
    tar -xvzf apache-tomcat-$tcversion.tar.gz && \
    mv apache-tomcat-$tcversion /tomcat && \
    rm -rf /tomcat/webapps/* && \
    mv jenkins.war /tomcat/webapps/ROOT.war && \
    rm -rf /tmp/* && \

    rm -rf /var/lib/apt/lists/* && \

    echo 'Done'

COPY ./default-start.sh /default-start.sh
RUN chmod +x /default-start.sh

CMD [ "/bin/sh", "-c", "/default-start.sh && sleep infinity" ]
