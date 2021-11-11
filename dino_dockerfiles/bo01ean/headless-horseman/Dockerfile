FROM ubuntu:16.04
MAINTAINER kelvin.beats@gmail.com
WORKDIR /tmp
RUN apt-get update
RUN apt-get install -y curl apt-utils xvfb wget default-jre vim git

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y --allow-unauthenticated nodejs
RUN apt-get install -y build-essential

RUN npm install -g protractor bower mocha jasmine n
RUN n 6.3.1
RUN webdriver-manager update

## Install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update
RUN apt-get install -y google-chrome-stable
## Clean up
RUN apt-get clean

ADD addUser.sh /addUser.sh
ADD protractor.sh /protractor.sh
ADD runtests.sh /runtests.sh

RUN /addUser.sh
RUN mkdir /protractor
ENV SCREEN_RES=1280x1024x24

WORKDIR /protractor
ENTRYPOINT ["/runtests.sh"]
