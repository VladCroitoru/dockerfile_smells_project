ARG SONAR_SCANNER_VERSION=3.1.0.1141
FROM gradle:4.6-jdk8-alpine as builder
ARG SONAR_SCANNER_VERSION
ENV GRADLE_USER_HOME /tmp
ENV SONAR_SCANNER_VERSION ${SONAR_SCANNER_VERSION}

USER root
WORKDIR /usr/src/myapp

COPY ./build.gradle /usr/src/myapp/
RUN gradle -PsonarScannerVersion=${SONAR_SCANNER_VERSION} downloadDependencies  --no-daemon --console plain
COPY ./src /usr/src/myapp/src
RUN gradle -PsonarScannerVersion=${SONAR_SCANNER_VERSION} build --no-daemon --console plain

FROM openjdk:8-jdk-alpine
ARG SONAR_SCANNER_VERSION

ARG HTTP_PORT=8080
ENV SONAR_SCANNER_HOME /usr/src/sonar-scanner
ENV PATH /usr/src/sonar-scanner:${PATH}
ENV HTTP_PORT ${HTTP_PORT}
ENV REPOS_PATH /tmp/temp_git_repos/
RUN apk add --update --no-cache git

WORKDIR /usr/src/myapp
COPY --from=builder /usr/src/myapp/build/libs/myapp.jar /usr/src/myapp/myapp.jar
COPY --from=builder /usr/src/myapp/gradle/repository/org/sonarsource/scanner/cli/sonar-scanner-cli/${SONAR_SCANNER_VERSION}/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.jar /usr/src/sonar-scanner/sonar-scanner-cli.jar
RUN ls -lah /usr/src/sonar-scanner/


RUN echo -e '#!/bin/sh\n\
java \
 -classpath $SONAR_SCANNER_HOME/sonar-scanner-cli.jar \
 $SONAR_SCANNER_OPTS \
 $SONAR_SCANNER_DEBUG_OPTS \
 org.sonarsource.scanner.cli.Main \
 -Djava.awt.headless=true \
 -Dscanner.home=$SONAR_SCANNER_HOME \
 -Dsonar.host.url=$SONAR_URL \
 -Dsonar.verbose=true \
 -Dsonar.issuesReport.console.enable=true \
 -Dsonar.login=$SONAR_TOKEN \
 $@ -X'\
> /usr/src/sonar-scanner/sonar-scanner

RUN chmod +x /usr/src/sonar-scanner/sonar-scanner
# a convenient empty direcotry to point for sonar.java.binaries 
# if trying to run sonar without java binaries pointing to empty directory would do
RUN mkdir -p /empty.sonar.java.binaries
EXPOSE ${HTTP_PORT}

CMD ["java","-jar","myapp.jar"]
