FROM ubuntu:16.04


LABEL name="ubuntu-chrome-chromedriver" \
			maintainer="Arturo Avilés <artcastell@gmail.com>" \
			version="1.0.0" \
			description="Ubuntu 16.04 with latest Chrome and ChromeDriver"


# User interaction is not desired
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true


# Prepare Ubuntu for new packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install wget -y \
	&& apt-get install curl -y \
	&& apt-get install unzip -y \
	&& apt-get install libxi6 libgconf-2-4 libnss3 -y


# Install Latest Google Chrome
# NOTICE: Google doesn't mantain old versions of google chrome.
#         If the container can't start Google Chrome, the Chrome Driver could have become incompatible.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && \
    apt-get install google-chrome-stable -y && \
    rm -rf /etc/apt/sources.list.d/google.list
# Check Google Chrome Version
RUN google-chrome-stable --version


# Install Latest Chrome Driver (The version can be changed in case the latest one is incompatible)
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver
# Check Chrome Driver Version
RUN chromedriver --version
