FROM kavabungo/docker-springxd-base
MAINTAINER Chernov Artur

USER root
ADD ./container_start.sh /opt/spring-xd/start
RUN chown springxd:springxd /opt/spring-xd/start
RUN chmod u+x /opt/spring-xd/start

#RUN yum install -y net-tools telnet curl wget nano

USER springxd

EXPOSE 8080
EXPOSE 8081

CMD ["/opt/spring-xd/start"]
