FROM maven:alpine
ENV JAVA_OPTS=-Xms256m\ -Xmx1g
COPY . /
RUN mvn -D skipTests=true install
VOLUME /tmp
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /target/github-trending-api-0.0.1-SNAPSHOT.jar
EXPOSE 8080
