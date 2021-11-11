FROM openjdk:11-jre-slim

WORKDIR /home/app

ADD ./target/*.jar ./app.jar

EXPOSE 8080
CMD java $JAVA_OPTS -Dspring.profiles.active=$PROFILE -Dserver.port=$PORT -jar app.jar
