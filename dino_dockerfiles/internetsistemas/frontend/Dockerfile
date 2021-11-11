FROM node:7

MAINTAINER [iS] <contato@internetsistemas.com.br>

RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN \
  apt-get update && \
  apt-get install -y xvfb google-chrome-stable rubygems && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN \
  gem install dpl --no-document

ADD xvfb.sh /etc/init.d/xvfb
ADD entrypoint.sh /entrypoint.sh

ENV DISPLAY :99
ENV CHROME_BIN /usr/bin/google-chrome

RUN \
  chmod +x /etc/init.d/xvfb && \
  chmod +x /entrypoint.sh

RUN npm install -g angular-cli node-sass phantomjs-prebuilt

ENTRYPOINT ["/entrypoint.sh"]
