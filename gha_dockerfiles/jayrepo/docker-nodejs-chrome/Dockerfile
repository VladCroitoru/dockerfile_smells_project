FROM node:current-slim

USER root

#============================================
# Dependencies
#============================================
RUN apt-get update -qqy \
    && apt-get -qqy install \
    wget \
    unzip \
    gnupg \
    xvfb \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

#============================================
# Google Chrome
#============================================
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qqy \
    && apt-get -qqy install google-chrome-stable \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/

#============================================
# chromedriver
#============================================
RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
    && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
    && wget -q -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && rm -rf /opt/selenium/chromedriver \
    && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod 755 /opt/selenium/chromedriver \
    && ln -fs /opt/selenium/chromedriver /usr/bin/chromedriver

#============================================
# node-gyp
#============================================
RUN apt-get update -qqy \
    && apt-get -qqy install \
    python \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
ENV DISPLAY :99

USER node
