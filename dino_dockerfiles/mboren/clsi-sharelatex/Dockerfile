FROM ubuntu:14.04

#RUN echo 'Acquire::HTTP::Proxy "http://172.17.42.1:3142";' >> /etc/apt/apt.conf.d/01proxy \
# && echo 'Acquire::HTTPS::Proxy "false";' >> /etc/apt/apt.conf.d/01proxy


RUN apt-get update && apt-get install -y software-properties-common python git

RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe"
RUN add-apt-repository ppa:chris-lea/node.js
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nodejs build-essential zlib1g-dev latexmk
RUN apt-get install -y texlive-latex-recommended texlive-latex-extra texlive-fonts-extra

# Install app dependencies
COPY package.json /src/package.json
RUN cd /src; npm install

RUN npm install -g grunt-cli

COPY Gruntfile.coffee /src/Gruntfile.coffee
RUN cd /src; grunt install

# Bundle app source
COPY . /src

EXPOSE 3013

WORKDIR /src
CMD ["grunt", "run"]