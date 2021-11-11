FROM openjdk:11-jre-slim
#LABEL maintainer="ensu6788@gmail.com"
ARG JAR_FILE=./build/libs/auth-0.0.1-SNAPSHOT.jar
ADD ${JAR_FILE} app.jar
COPY ./elastic-apm-agent-*.jar /elastic-apm-agent.jar
EXPOSE 6000
ENTRYPOINT java -server -Djava.security.egd=file:/dev/./uradom ${JAVA_OPTIONS} -jar /app.jar
##ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./uradom","${JAVA_OPTIONS}","-jar","/app.jar"]
