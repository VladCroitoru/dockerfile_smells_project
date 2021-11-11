FROM openjdk:11
VOLUME /tmp
ARG JAR_FILE=build/libs/elaastic-questions-server-4.1.0.jar
ARG CONF_FILE=docker-resources/elaastic-questions/elaastic-questions.properties
ADD ${JAR_FILE} elaastic-questions.jar
ADD ${CONF_FILE} elaastic-questions.properties

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-Dspring.config.additional-location=/elaastic-questions.properties","-jar","/elaastic-questions.jar"]
