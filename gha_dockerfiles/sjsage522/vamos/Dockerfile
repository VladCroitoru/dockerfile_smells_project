FROM openjdk:11

ADD ./build/libs/vamos-0.0.1-SNAPSHOT.jar /usr/src/vamos-0.0.1-SNAPSHOT.jar
WORKDIR usr/src

ENTRYPOINT ["java", "-jar", "vamos-0.0.1-SNAPSHOT.jar"]