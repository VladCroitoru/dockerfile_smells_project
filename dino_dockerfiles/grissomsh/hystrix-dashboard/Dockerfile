FROM airdock/oracle-jdk:latest

MAINTAINER Grissom Wang <grissom.wang@daocloud.io>

ENV TIME_ZONE Asia/Shanghai

RUN echo "$TIME_ZONE" > /etc/timezone

WORKDIR /app

RUN apt-get update

RUN curl --insecure https://repo1.maven.org/maven2/com/netflix/hystrix/hystrix-dashboard/1.5.9/hystrix-dashboard-1.5.9.war -o hystrix-dashboard.war

RUN curl --insecure https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-runner/9.4.1.v20170120/jetty-runner-9.4.1.v20170120.jar -o jetty-runner.jar

EXPOSE 8080

CMD [ "java", "-jar", "jetty-runner.jar", "hystrix-dashboard.war" ]
