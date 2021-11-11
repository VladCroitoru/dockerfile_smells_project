FROM google/nodejs:0.10.33

MAINTAINER Joseph M. "joe@teneleven.co.uk"

RUN apt-get update
RUN apt-get install -y python-software-properties python build-essential curl libfreetype6 libfontconfig git-core
RUN apt-get install -y libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++
RUN apt-get install -y graphicsmagick
RUN npm install -g grunt-cli phantomjs bower coffee-script gulp
RUN apt-get install -y ruby-dev
RUN gem install sass -v 3.4.13

