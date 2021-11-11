FROM ubuntu:14.04
MAINTAINER Alessio Garzi "gun101@email.it"


RUN apt-get update

#RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
#RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

# Install nodejs
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get install -y nodejs

# install modules
RUN npm install -g grunt-cli
RUN npm install -g bower
RUN npm install grunt --save-dev
RUN npm install grunt-contrib-uglify
RUN npm install grunt-contrib-jshint 
RUN npm install grunt-contrib-concat
RUN npm install grunt-contrib-watch
RUN npm install grunt-contrib-jade
RUN npm install grunt-contrib-less
RUN npm install grunt-contrib-connect 
RUN npm install grunt-contrib-copy 
RUN npm install grunt-contrib-coffee
RUN npm install grunt-sitemap
RUN npm install grunt-modernizr

# pull website
RUN apt-get install -y git
ENV LOL=lol
RUN git clone https://github.com/Ozzyboshi/InternetBeatTimeWatchfaceWebsite
RUN cd InternetBeatTimeWatchfaceWebsite && ./lin-install.sh && ./lin-dev-build.sh

EXPOSE 9000
CMD cd InternetBeatTimeWatchfaceWebsite && grunt serve
