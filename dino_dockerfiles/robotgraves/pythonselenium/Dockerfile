FROM ubuntu:16.04
LABEL authors="Alex Paul,John Nolette <john@neetgroup.net>"

# http://bugs.python.org/issue19846

ENV LANG C.UTF-8

# APT-GET REPOSITORIES

RUN  echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" > /etc/apt/sources.list \
  && echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n" >> /etc/apt/sources.list \
  && echo "deb http://security.ubuntu.com/ubuntu xenial-security main universe\n" >> /etc/apt/sources.list

# NO INTERACTIVE FRONTEND DURING BUILD

ENV DEBIAN_FRONTEND=noninteractive \
DEBCONF_NONINTERACTIVE_SEEN=true

# IMAGE UTILITIES

ENV PATH /usr/local/bin:$PATH

RUN apt-get update && apt-get install -qqy -y --no-install-recommends \
    ca-certificates libgdbm3 libsqlite3-0 libssl1.0.0 python-setuptools python-dev build-essential wget \
    curl zip unzip bzip2 zlib1g-dev libopenjpeg-dev libjpeg-dev

ADD virenv /tmp

RUN tar -xzvpf /tmp/virtualenv-15.0.0.tar.gz -C /tmp \
    && python /tmp/virtualenv-15.0.0/virtualenv.py /opt/v \
    && rm -rf /tmp/virtualenv-15.0.0

RUN /opt/v/bin/pip install pyyaml

# FIREFOX BROWSER

ARG FIREFOX_VERSION=58.0.2
RUN FIREFOX_DOWNLOAD_URL=$(if [ $FIREFOX_VERSION = "nightly" ] || [ $FIREFOX_VERSION = "devedition" ]; then echo "https://download.mozilla.org/?product=firefox-$FIREFOX_VERSION-latest-ssl&os=linux64&lang=en-US"; else echo "https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2"; fi) \
    && apt-get update -qqy \
    && apt-get -qqy --no-install-recommends install firefox firefox-dbg \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
    && wget --no-verbose -O /tmp/firefox.tar.bz2 $FIREFOX_DOWNLOAD_URL \
    && apt-get -y purge firefox \
    && rm -rf /opt/firefox \
    && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
    && rm /tmp/firefox.tar.bz2 \
    && mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \
    && ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox

# GECKODRIVER

ARG GECKODRIVER_VERSION=0.19.1
RUN GK_VERSION=$(if [ ${GECKODRIVER_VERSION:-latest} = "latest" ]; then echo $(wget -qO- "https://api.github.com/repos/mozilla/geckodriver/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([0-9.]+)".*/\1/'); else echo $GECKODRIVER_VERSION; fi) \
    && echo "Using GeckoDriver version:" $GK_VERSION \
    && wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GK_VERSION/geckodriver-v$GK_VERSION-linux64.tar.gz \
    && rm -rf /opt/geckodriver \
    && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
    && rm /tmp/geckodriver.tar.gz \
    && mv /opt/geckodriver /opt/geckodriver-$GK_VERSION \
    && chmod 755 /opt/geckodriver-$GK_VERSION \
    && ln -fs /opt/geckodriver-$GK_VERSION /usr/bin/geckodriver

# CHROME BROWSER

ARG CHROME_VERSION="google-chrome-stable=65.0.3325.146-1"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qqy \
    && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable} \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# CHROME DRIVER

ARG CHROME_DRIVER_VERSION=2.35
RUN CD_VERSION=$(if [ ${CHROME_DRIVER_VERSION:-latest} = "latest" ]; then echo $(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else echo $CHROME_DRIVER_VERSION; fi) \
    && echo "Using chromedriver version: "$CD_VERSION \
    && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip \
    && rm -rf /opt/selenium/chromedriver \
    && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
    && rm /tmp/chromedriver_linux64.zip \
    && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CD_VERSION \
    && chmod 755 /opt/selenium/chromedriver-$CD_VERSION \
    && ln -fs /opt/selenium/chromedriver-$CD_VERSION /usr/bin/chromedriver
