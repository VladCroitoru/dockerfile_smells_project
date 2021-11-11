### Multi-stage Docker file - maven build for java ###

## Stage 1/2 - Build fat JAR file with maven
FROM harbor.example.com/library/java/maven:3-jdk-8-slim as builder

RUN mkdir -p /build
WORKDIR /build
COPY pom.xml /build

# download all required dependencies into a single layer that won't change unless there's a change in pom.xml
RUN mvn dependency:go-offline -B 
# RUN mvn -B dependency:resolve dependency:resolve-plugins

#Copy source code
COPY src /build/src

# Build application
RUN mvn package -DAPP_VERSION=v1.0 -DskipTests


## Stage 2/2 - Containerize the standalone JAR application
FROM harbor.example.com/library/suse/sles15sp3-openjdk:11.0-3.56.1 as runtime
EXPOSE 8080

ENV APP_HOME /app
ENV JAVA_OPTS=""

RUN mkdir $APP_HOME
# store externalized config files and logs
RUN mkdir $APP_HOME/config
RUN mkdir $APP_HOME/log

VOLUME $APP_HOME/config
VOLUME $APP_HOME/log

WORKDIR $APP_HOME
COPY --from=builder /build/target/*.jar app.jar

ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar app.jar $0 $@" ]
