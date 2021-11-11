FROM java:8

ADD target/ticketingservice-1.0.1-RELEASE.jar app.jar

RUN sh -c 'touch /app.jar'

EXPOSE 8090

ENV JAVA_OPTS=""

ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]
