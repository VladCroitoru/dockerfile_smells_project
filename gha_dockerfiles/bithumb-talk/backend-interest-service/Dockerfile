FROM openjdk:17-ea-11-jdk-slim
VOLUME /server
ARG JAR_FILE=./build/libs/interest-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} interest.jar
EXPOSE 5000
#ENTRYPOINT ["java","-Dspring.data.mongodb.uri=mongodb://mongo/test","-Djava.security.egd=file:/dev/./urandom","-jar","/interest.jar"]
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/interest.jar"]
