FROM openjdk:8-jre-alpine

ENV JHIPSTER_SLEEP 0

# add directly the war
ADD target/back-end.jar /app.jar

RUN sh -c 'touch /app.jar'
VOLUME /tmp
EXPOSE 8080
CMD echo "The application will start in ${JHIPSTER_SLEEP}s..." && \
    sleep ${JHIPSTER_SLEEP} && \
    java -Djava.security.egd=file:/dev/./urandom -jar /app.jar
