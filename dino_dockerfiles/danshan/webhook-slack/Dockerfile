FROM maven:3.3.9-jdk-8
MAINTAINER Dan <i@shanhh.com>

ENV SERVER_PORT 8080
ENV SLACK_DAOCLOUD slack_daocloud
ENV SLACK_MICROBADGER slack_microbadger
ENV SLACK_DOCKER slack_docker
ENV SLACK_SONARQUBE slack_sonarqube
ENV SLACK_CODING slack_coding

ENV PROJ_DIR /tmp/project
ENV JAR_PATH ${PROJ_DIR}/target/application.jar
ENV DIST_DIR /var/lib/app
RUN mkdir -p ${DIST_DIR}

ADD . ${PROJ_DIR}
WORKDIR ${PROJ_DIR}
RUN mvn package
RUN cp ${JAR_PATH} ${DIST_DIR}/application.jar

RUN rm -rf /etc/localtime && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' > /etc/timezone

EXPOSE ${SERVER_PORT}
ENTRYPOINT ["/bin/sh", "-c", "java -Dfile.encoding=UTF8 -Duser.timezone=GMT+08 -Dserver.port=${SERVER_PORT} -Dslack.daocloud=${SLACK_DAOCLOUD} -Dslack.microbadger=${SLACK_MICROBADGER} -Dslack.docker=${SLACK_DOCKER} -Dslack.sonarqube=${SLACK_SONARQUBE} -Dslack.coding=${SLACK_CODING} -Djava.security.egd=file:/dev/./urandom -jar ${DIST_DIR}/application.jar"]
