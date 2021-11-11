FROM ruby:3.0.2

ENV LANG ja_JP.UTF-8

WORKDIR /webapp

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && sh -c 'wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
  && CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` \
  && wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/ \
  && unzip ~/chromedriver_linux64.zip -d ~/ \
  && rm ~/chromedriver_linux64.zip \
  && chown root:root ~/chromedriver \
  && chmod 755 ~/chromedriver \
  && mv ~/chromedriver /usr/bin/chromedriver \
  && apt-get update -qq && apt-get install -y build-essential google-chrome-stable \
  && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
  && apt-get install -y nodejs \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && gem install bundler sqlite3 pry pry-coolline