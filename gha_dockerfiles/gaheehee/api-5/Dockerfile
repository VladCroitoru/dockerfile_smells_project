FROM openjdk:8
LABEL maintainer="jghgahee@ajou.ac.kr"
ENV mysql_address matzipfive.cnj8s2utcsrc.ap-northeast-2.rds.amazonaws.com
ENV mysql_username wave
ENV mysql_password 여기 채워야함.
ARG JAR_FILE=build/libs/firstproject-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
EXPOSE 8088
