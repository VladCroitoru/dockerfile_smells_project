FROM node:7.10-slim
MAINTAINER j.ciolek@webnicer.com
WORKDIR /tmp
COPY webdriver-versions.js ./
ENV CHROME_PACKAGE="google-chrome-stable_55.0.2883.75-1_amd64.deb" NODE_PATH=/usr/local/lib/node_modules
RUN npm install -g protractor@5.1.1 mocha@3.3.0 jasmine@2.5.3 minimist@1.2.0 && \
    node ./webdriver-versions.js --chromedriver 2.27 && \
    webdriver-manager update && \
    apt-get update && \
    apt-get install -y xvfb wget openjdk-7-jre && \
    wget https://github.com/webnicer/chrome-downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \
    dpkg --unpack ${CHROME_PACKAGE} && \
    apt-get install -f -y && \
    apt-get clean && \
    rm ${CHROME_PACKAGE} && \
    mkdir /protractor
COPY protractor.sh /protractor.sh
ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
RUN apt-get install build-essential chrpath libssl-dev libxft-dev -y && \
    apt-get install libfreetype6 libfreetype6-dev -y && \
    apt-get install libfontconfig1 libfontconfig1-dev -y && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 && \
    tar xvjf $PHANTOM_JS.tar.bz2 && \
    mv $PHANTOM_JS /usr/local/share && \
    ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
# Fix for the issue with Selenium, as described here:
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
ENV SCREEN_RES=1280x1024x24
WORKDIR /protractor
ENTRYPOINT ["/protractor.sh"]
