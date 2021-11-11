FROM openjdk:8-jdk-alpine

RUN mkdir /build
ADD . /build
WORKDIR /build
RUN chmod +x mvnw
RUN ./mvnw clean install
RUN mv target/*.jar /app.jar
WORKDIR /
RUN rm -r /build
RUN rm -r /root/.m2

ENTRYPOINT exec java $JAVA_OPTS -jar /app.jar
