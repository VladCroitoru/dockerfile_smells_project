#FROM openjdk:8-jdk-alpine
#VOLUME /tmp
#ARG DEPENDENCY=target/dependency
#COPY ${DEPENDENCY}/BOOT-INF/lib /app/lib
#COPY ${DEPENDENCY}/META-INF /app/META-INF
#COPY ${DEPENDENCY}/BOOT-INF/classes /app
#ENTRYPOINT ["java","-cp","app:app/lib/*","com.sample.Application"]

FROM java:8-jdk-alpine
COPY ./target/spring-boot-docker-0.0.1-SNAPSHOT.jar /usr/app/
WORKDIR /usr/app
RUN sh -c 'touch spring-boot-docker-0.0.1-SNAPSHOT.jar'
ENTRYPOINT ["java","-jar","spring-boot-docker-0.0.1-SNAPSHOT.jar"]