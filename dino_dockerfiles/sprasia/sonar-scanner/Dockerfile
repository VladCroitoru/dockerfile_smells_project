FROM openjdk:8-alpine

ENV SONARQUBE_SCANNER_VERSION "3.2.0.1227"

LABEL maintainer="Willie Loyd Tandingan <n3v3rf411@gmail.com>"

RUN addgroup -g 1000 sonar && \
    adduser -u 1000 -G sonar -s /bin/sh -D sonar


RUN set -x && \
  apk add --no-cache curl grep sed unzip nodejs nodejs-npm && \
  curl --insecure -o ./sonarscanner.zip -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONARQUBE_SCANNER_VERSION}-linux.zip && \
  unzip sonarscanner.zip && \
  rm sonarscanner.zip && \
  rm sonar-scanner-${SONARQUBE_SCANNER_VERSION}-linux/jre -rf && \
#   ensure Sonar uses the provided Java for musl instead of a borked glibc one
  sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' sonar-scanner-${SONARQUBE_SCANNER_VERSION}-linux/bin/sonar-scanner && \
  chown -R sonar.sonar sonar-scanner-${SONARQUBE_SCANNER_VERSION}-linux

ENV SONAR_RUNNER_HOME=/sonar-scanner-${SONARQUBE_SCANNER_VERSION}-linux
ENV PATH $PATH:/sonar-scanner-${SONARQUBE_SCANNER_VERSION}-linux/bin

COPY sonar-runner.properties /sonar-scanner-${SONARQUBE_SCANNER_VERSION}-linux/conf/sonar-scanner.properties

USER sonar
CMD sonar-scanner
