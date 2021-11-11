FROM openjdk:8-jre-alpine

ENV SONAR_SCANNER_VERSION 4.3.0.2102-linux
ENV SONARDIR /var/opt/sonar-scanner-${SONAR_SCANNER_VERSION}
ENV SONARBIN ${SONARDIR}/bin/sonar-scanner

RUN apk add --update --no-cache wget nodejs && \
    cd /var/opt/ && \
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    rm -rf ${SONARDIR}/jre && \
    sed -i -e 's/use_embedded_jre=true/use_embedded_jre=false/' ${SONARBIN} ${SONARBIN}-debug && \
    ln -s ${SONARBIN} /usr/bin/sonar-scanner && \
    apk del wget

COPY sonar-scanner-run.sh /usr/bin/
