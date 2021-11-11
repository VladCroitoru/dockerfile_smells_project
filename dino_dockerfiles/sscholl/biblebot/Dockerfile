FROM openjdk:8-jdk-alpine
MAINTAINER Simon Scholl <s@sdscholl.de>

########################################################
# build generic spring boot app

ARG mvnArgs="-B -T 1C -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn"
ARG skipTests=true

# download dependencies and provide docker layer as cache for later builds
COPY pom.xml mvnw /tmp/
COPY .mvn /tmp/.mvn
RUN cd /tmp && sh ./mvnw ${mvnArgs} dependency:go-offline

# generate app by maven and clear maven and build folder
COPY . /tmp
RUN cd /tmp && sh ./mvnw clean install ${mvnArgs} -DskipTests=${skipTests}
RUN mv /tmp/target/*.jar /app.jar \
    && rm /tmp/* -rf \
    && rm /tmp/.git* -rf \
    && rm /tmp/.mvn -rf \
    && rm /root/.m2 -rf

# unzip app, because some spring boot apps have problems with resources when using jersey
RUN mkdir /app \
    && unzip -q /app.jar -d /app \
    && rm /app.jar

########################################################
# custom environment variables
ENV BIBLEBOT_INTEGRATION_HOST ""
ENV BIBLEBOT_INTEGRATION_PORT 8080
ENV BIBLEBOT_API_HOST ""
ENV BIBLEBOT_API_PORT ""

#ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
CMD java -cp /app org.springframework.boot.loader.JarLauncher --server.port=${BIBLEBOT_INTEGRATION_PORT} -Djava.security.egd=file:/dev/./urandom