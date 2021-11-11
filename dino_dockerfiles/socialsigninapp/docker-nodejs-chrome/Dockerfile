# docker build --build-arg http_proxy=http://192.168.0.66:3128 --build-arg https_proxy=http://192.168.0.66:3128 .

FROM node:10-stretch

ARG http_proxy=""
ARG https_proxy=""
ARG DEBIAN_FRONTEND=noninteractive

# Xvfb
RUN apt-get update -qqy && \
    apt-get install -y eatmydata && \
	eatmydata -- apt-get -qqy install xvfb && \
	apt-get clean && rm -rf /var/lib/apt/lists/* 

# Google Chrome

RUN wget -q -O /tmp/key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub \
    && apt-key add /tmp/key.asc \
	&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get -qqy update \
	&& eatmydata -- apt-get -qqy install google-chrome-stable \
	&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
	&& sed -i 's/"$HERE\/chrome"/xvfb-run "$HERE\/chrome" --no-sandbox/g' /opt/google/chrome/google-chrome

WORKDIR /workspace
