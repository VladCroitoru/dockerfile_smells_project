from ubuntu:14.04

MAINTAINER rockets "rockets.fang@gmail.com"

ENV CATALINA_BASE /var/lib/tomcat7
ENV CATALINA_HOME /usr/share/tomcat7

RUN apt-get update && apt-get install -y openssh-server curl tomcat7 && mkdir -p /var/run/sshd

RUN echo "root:123456" | chpasswd

COPY ./report.war $CATALINA_BASE/webapps

RUN $CATALINA_HOME/bin/catalina.sh start && sleep 5 && $CATALINA_HOME/bin/catalina.sh stop

ADD ./data $CATALINA_BASE/webapps/report/data

EXPOSE 22

EXPOSE 8080

ENTRYPOINT $CATALINA_HOME/bin/catalina.sh run
