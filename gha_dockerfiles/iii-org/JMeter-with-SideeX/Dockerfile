FROM node:14.18.0-buster

ENV JMETER_FOLDER=/apache-jmeter
ENV SELENIUM_FOLDER=/selenium_server
ENV JPGC_PERFMON_VERSION=2.1
ENV APACHE_JMETER_VERSION=5.2.1
ENV SELENIUM_GRID_VERSION=3.141.59
ENV CHROME_DRIVER_VERSION=94.0.4606.61

## 提供預設參數位置(ARG)
ENV JMETER_HISTORY_FOLDER_NAME=jmeterHistory
ENV JMETER_JMX_FILE_NAME='Test-Plan.jmx'

## 安裝套件
RUN apt-get -y update && apt install -y openjdk-11-jdk apt-utils tree
RUN npm i -g @sideex/runner debug
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb

## 下載單機版本的selenium
## https://hackmd.io/@sideex/book-zh/%2F%40sideex%2Fwebdriver-zh#Here-are-the-browsers-currently-supported-by-SideeX
## https://chromedriver.chromium.org/downloads
RUN mkdir -p ${SELENIUM_FOLDER}
WORKDIR ${SELENIUM_FOLDER}
RUN wget https://github.com/SeleniumHQ/selenium/releases/download/selenium-${SELENIUM_GRID_VERSION}/selenium-server-standalone-${SELENIUM_GRID_VERSION}.jar && \
    wget https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip -l chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    tree
RUN chmod -R 777 ${SELENIUM_FOLDER}

## >>>>> 下載Jmeter與其Plugin
WORKDIR /tmp
## 下載Jmeter
RUN wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-${APACHE_JMETER_VERSION}.tgz && \
    tar zxvf apache-jmeter-${APACHE_JMETER_VERSION}.tgz && \
    mv apache-jmeter-${APACHE_JMETER_VERSION} ${JMETER_FOLDER};
## 下載Jmeter額外Plugin
RUN wget https://jmeter-plugins.org/files/packages/jpgc-perfmon-${JPGC_PERFMON_VERSION}.zip && \
    unzip -l jpgc-perfmon-${JPGC_PERFMON_VERSION}.zip && \
    unzip jpgc-perfmon-${JPGC_PERFMON_VERSION}.zip -d ${JMETER_FOLDER}
## 目前Jmeter完整資料
RUN cd ${JMETER_FOLDER}

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 777 /docker-entrypoint.sh
COPY example /app
ENTRYPOINT ["/docker-entrypoint.sh"]
