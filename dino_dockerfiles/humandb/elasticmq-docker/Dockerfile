FROM centos:6.7
MAINTAINER Javier Lopez <f12loalf@gmail.com>

EXPOSE 9324

ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-0.8.11.jar /usr/share/elasticmq-server-0.8.11.jar
RUN yum install -y java-1.7.0-openjdk

CMD ["java", "-jar", "/usr/share/elasticmq-server-0.8.11.jar"]

