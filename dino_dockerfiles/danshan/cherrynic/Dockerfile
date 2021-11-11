FROM maven:3.3.9-jdk-8
MAINTAINER Dan <i@shanhh.com>

ENV SERVER_PORT 8080
ENV DAOCLOUD_TOKEN token
ENV CHERRYNIC_DATABASE_URL jdbc:mysql://mysql:3306/cherrynic?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&verifyServerCertificate=false
ENV CHERRYNIC_DATABASE_USERNAME username
ENV CHERRYNIC_DATABASE_PASSWORD password

ENV PROJ_DIR /tmp/project
ENV JAR_PATH ${PROJ_DIR}/cherrynic-web/target/application.jar
ENV DIST_DIR /var/lib/app
RUN mkdir -p ${DIST_DIR}

ADD . ${PROJ_DIR}
WORKDIR ${PROJ_DIR}
RUN mvn package
RUN cp ${JAR_PATH} ${DIST_DIR}/application.jar

RUN rm -rf /etc/localtime && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' > /etc/timezone

EXPOSE ${SERVER_PORT}
ENTRYPOINT ["/bin/sh", "-c", "java -Dfile.encoding=UTF8 -Duser.timezone=GMT+08 -Dserver.port=${SERVER_PORT} -Dcn.daocloud.token=${DAOCLOUD_TOKEN} -Dspring.datasource.url=${CHERRYNIC_DATABASE_URL} -Dspring.datasource.username=${CHERRYNIC_DATABASE_USERNAME} -Dspring.datasource.password=${CHERRYNIC_DATABASE_PASSWORD} -Djava.security.egd=file:/dev/./urandom -jar ${DIST_DIR}/application.jar"]
