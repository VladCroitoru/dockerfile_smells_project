FROM maven:3.3.9-jdk-7

MAINTAINER JMcn <411164348@qq.com>

ADD pom.xml /root/pom.xml
ADD src /root/src

WORKDIR /root

EXPOSE 80 8080

RUN mvn compile
RUN mvn package
