FROM openjdk:8u302-jdk-slim

VOLUME /tmp

EXPOSE 8083

COPY Wallet_restdatabase /usr/local/share/Wallet_restdatabase

ADD *.jar app.jar

ENV JAVA_OPTS=""

ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]