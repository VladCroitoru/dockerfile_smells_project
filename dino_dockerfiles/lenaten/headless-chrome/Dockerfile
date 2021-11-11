FROM ubuntu:16.04

RUN set -xe \
  && apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN set -xe \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 9222

ENTRYPOINT [ "google-chrome" ]