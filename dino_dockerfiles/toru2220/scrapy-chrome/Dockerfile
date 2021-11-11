FROM python:3

RUN 	LATEST_RELEASE_VERSION=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
	&& curl -SLO http://chromedriver.storage.googleapis.com/$LATEST_RELEASE_VERSION/chromedriver_linux64.zip \
	&& unzip chromedriver_linux64.zip -d /usr/local/bin \
	&& chmod 755 /usr/local/bin/chromedriver \
  	&& rm chromedriver_linux64.zip

RUN apt update \
	&& apt install -y fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatspi2.0-0 libgtk-3-0 libnspr4 libnss3 libx11-xcb1 libxtst6 lsb-release xdg-utils

RUN curl -SLO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
	&& dpkg -i google-chrome-stable_current_amd64.deb \
  	&& rm google-chrome-stable_current_amd64.deb

RUN     apt-get update && \
        apt-get install -y --no-install-recommends wget curl unzip fontconfig xvfb imagemagick ffmpeg

RUN     apt-get update && \
        apt-get install -y --no-install-recommends python3-dev python3-pip python-twisted libxml2-dev python-lxml python-requests nodejs && \
        rm -rf /var/lib/apt/lists/*
RUN     pip3 install pymongo urllib3 requests scrapy mpegdash m3u8 fake-useragent twython mojimoji pillow slackweb lxml slack_log_handler chromedriver-binary scrapy-splash selenium nodejs pathvalidate && \
        pip3 install git+https://github.com/yashaka/selene.git

WORKDIR /data
VOLUME  /data

COPY    IPAfont00303.zip /data/IPAfont00303.zip

RUN     unzip IPAfont00303.zip -d /usr/share/fonts/ && \
        fc-cache -fv

