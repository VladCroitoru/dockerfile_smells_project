FROM openjdk:11
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} classic-music.jar
ENTRYPOINT ["java","-jar","/classic-music.jar"]
