FROM anapsix/alpine-java:8_jdk
LABEL maintainer="United Classifieds <unitedclassifiedsapps@gmail.com>"

ENV HOME "/root"
WORKDIR ${HOME}

ENV SONAR_SCANNER_VERSION 3.0.3.778
ENV SONAR_LINT_VERSION 2.1.0.566

ENV PATH "$PATH:${HOME}/sonar-scanner/bin:${HOME}/sonarlint-cli/bin:${HOME}/bin"

RUN apk update && apk add --no-cache \
    bash \
    unzip \
    git \
    && rm -rf /tmp/* /var/tmp/*

ADD https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip sonar-scanner.zip
RUN unzip sonar-scanner.zip && rm sonar-scanner.zip && mv sonar-scanner-${SONAR_SCANNER_VERSION} sonar-scanner

ADD scan bin/scan
RUN chmod u+x bin/scan