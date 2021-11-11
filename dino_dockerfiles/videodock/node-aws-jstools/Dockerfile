FROM node:7.8-alpine
MAINTAINER Videodock <tech@videodock.com>

RUN apk update && apk upgrade

# update vim and wget only for in container editing
RUN apk --update add python-dev ruby ruby-dev curl git gcc alpine-sdk libffi-dev openssh && rm /var/cache/apk/*

# install grunt, gulp and bower
RUN npm install grunt-cli gulp-cli bower -g
RUN npm install cordova@8.0.0 -g

# install sass and compass
RUN gem install --no-rdoc --no-ri sass -v 3.4.22
RUN gem install --no-rdoc --no-ri compass -v 1.0.3

# install aws cli
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install awscli
