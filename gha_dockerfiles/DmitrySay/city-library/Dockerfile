FROM openjdk:11

ENV JAVA_OPTS=""

WORKDIR /opt

COPY /build/libs/city-library.jar .

EXPOSE 8080

CMD java ${JAVA_OPTS} -jar city-library.jar
