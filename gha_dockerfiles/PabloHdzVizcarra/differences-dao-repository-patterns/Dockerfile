FROM amazoncorretto:11-alpine-jdk

LABEL maintainer="pablohernandez.jvm"

ADD target/*.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]