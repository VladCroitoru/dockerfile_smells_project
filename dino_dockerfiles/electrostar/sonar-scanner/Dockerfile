FROM openjdk:8-jdk-alpine
ENV SONAR_SCANNER_VERSION 3.3.0.1492

RUN apk add --no-cache wget && \
    apk add --no-cache git && \  
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \  
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \  
    cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner sonar-scanner && \  
    apk del wget && \
    rm /sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    git config --global user.email "you@example.com" && \
    git config --global user.name "Testuser"
