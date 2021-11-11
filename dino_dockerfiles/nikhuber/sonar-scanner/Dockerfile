FROM openjdk:8-jre-alpine

LABEL maintainer="Nikolaus Huber <docker.niko_huber@mailhero.io>"

ARG SONAR_SCANNER_VERSION="3.0.3.778"

RUN apk add --no-cache curl sed unzip nodejs

# Settings
ENV SONAR_URL="https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip"
ENV SONAR_RUNNER_HOME="/opt/sonar-scanner-${SONAR_SCANNER_VERSION}-linux"
ENV PATH $PATH:$SONAR_RUNNER_HOME/bin

RUN mkdir -p /opt
WORKDIR /opt

# Install sonar-scanner
RUN curl -o ./sonarscanner.zip -L $SONAR_URL
RUN unzip sonarscanner.zip 
RUN rm sonarscanner.zip

# Ensure Sonar Scanner uses openjdk instead of the packaged JRE (which is broken)
RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' $SONAR_RUNNER_HOME/bin/sonar-scanner

COPY printScannerConfig.sh /opt
RUN chmod +x /opt/printScannerConfig.sh

CMD [ "/opt/printScannerConfig.sh" ]
