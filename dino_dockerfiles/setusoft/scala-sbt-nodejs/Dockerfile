FROM hseeberger/scala-sbt:latest

MAINTAINER setusoft <christian.kaps@setusoft.de>

ENV DISPLAY :99.0
ENV CHROME_BIN /usr/bin/google-chrome
ENV SONAR_SCANNER_VERSION 3.2.0.1227

RUN apt-get update && \
    apt-get install -y rpm && \
    apt-get install -y git && \
    apt-get install -y openssl && \
    apt-get install -y bsdmainutils

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install yarn

RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \
    ln -s /root/sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner /usr/bin/sonar-scanner

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg --unpack google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

RUN apt-get install -f -y && \
    apt-get clean
