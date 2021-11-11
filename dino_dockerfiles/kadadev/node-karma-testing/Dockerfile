FROM kadadev/node-small:latest

RUN apk add --no-cache xvfb dbus ttf-freefont udev openjdk8-jre-base
RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community chromium chromium-chromedriver
RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing firefox

ENV DISPLAY :99
ENV CHROME_BIN /usr/bin/chromium

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
