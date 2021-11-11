FROM java:8-alpine

MAINTAINER Matthew Tardiff <mattrix@gmail.com>

RUN apk add --update curl unzip && \
    rm -rf /var/cache/apk/*

ENV SONAR_VERSION 2.6.1
ENV SONAR_DIR sonar-scanner-$SONAR_VERSION
ENV SONAR_ZIP sonar-scanner-$SONAR_VERSION.zip

RUN curl -o $SONAR_ZIP -L https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/$SONAR_ZIP && \
    unzip $SONAR_ZIP && \
    rm $SONAR_ZIP && \
    mv $SONAR_DIR sonar-scanner

VOLUME /src
WORKDIR /src

ENTRYPOINT ["/sonar-scanner/bin/sonar-scanner"]
