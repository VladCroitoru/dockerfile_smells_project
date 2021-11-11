FROM ubuntu

ENV NODE_VERSION v7.2.1

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y python python-dev python-pip python3 python3-dev python3-pip \
                                                      curl git build-essential libssl-dev ruby-dev \
                                                      libpq-dev libmysqlclient-dev \
                                                      libjpeg8-dev zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*
RUN pip install git+https://github.com/jonls/s3-deploy-website
#RUN git clone https://github.com/creationix/nvm.git /.nvm

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install wget
RUN apt-get install -f

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt-get -y install google-chrome-stable

RUN apt-get -y install nodejs
RUN apt-get -y install npm
RUN ln -s `which nodejs` /usr/bin/node

RUN apt-get install -y xvfb
RUN apt-get install -y openjdk-8-jdk

RUN npm install -g s3-deploy
RUN npm install -g --save-dev webdriverio
RUN npm install -g --save-dev wdio-cucumber-framework
RUN npm install selenium-standalone@latest -g
