FROM openjdk:11
LABEL maintainer=p@fts.nl
WORKDIR /app
ARG JAR_FILE=target/EasyContacts-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} /app/EasyContactsAPI.jar
ENTRYPOINT ["java","-jar","EasyContactsAPI.jar"]