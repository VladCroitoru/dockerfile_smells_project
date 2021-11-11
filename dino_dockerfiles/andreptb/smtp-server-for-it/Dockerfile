FROM andreptb/oracle-java:8-alpine

ENV JAVA_OPTS -Djava.security.egd=file:/dev/./urandom

EXPOSE 80
EXPOSE 8009

RUN apk update && apk add --no-cache wget \
    && wget -q --no-check-certificate https://github.com/andreptb/smtp-server-for-it/releases/download/v0.2.0/smtp-server-for-it.jar -O smtp-server-for-it.jar \
    && apk del wget

CMD ["java", "-jar", "smtp-server-for-it.jar"]
