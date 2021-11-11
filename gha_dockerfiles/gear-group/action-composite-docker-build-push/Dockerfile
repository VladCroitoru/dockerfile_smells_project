FROM openjdk:8-jre-alpine
RUN apk add --no-cache fontconfig ttf-dejavu

ENV SPRING_OUTPUT_ANSI_ENABLED=ALWAYS \
    STARTUP_SLEEP=0 \
    JAVA_OPTS=""

CMD echo "The application will start in ${STARTUP_SLEEP}s..." && \
    echo "With Java opts: ${JAVA_OPTS}" && \
    sleep ${STARTUP_SLEEP} && \
    java ${JAVA_OPTS} -Djava.security.egd=file:/dev/./urandom -jar /app.jar

EXPOSE 8080

ADD *.jar /app.jar