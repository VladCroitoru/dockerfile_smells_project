FROM ubuntu:latest
MAINTAINER Matt Koski <maccam912@gmail.com>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

RUN apt-get update 
#RUN apt-get install -y mongodb-org
RUN apt-get install -y mongodb-org git python python3-pip build-essential curl
RUN service mongod start

RUN mkdir -p /data/db

RUN mkdir /Development
RUN cd /Development && git clone --branch v0.12.7 git://github.com/nodejs/node

RUN cd /Development/node && ./configure && make && make install
RUN rm -rf /Development/node
RUN chmod 777 -R /Development

RUN npm install -g yo bower grunt-cli generator-meanjs express
RUN alias python=python3

# RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh

EXPOSE 80:80
EXPOSE 443:443
EXPOSE 3000:3000



RUN echo "\n##############################\n1. Create a new user with adduser, 'su' into that user.\n2. 'yo meanjs' to scaffold your app in the current directory.\n3. Start mongo in the background (e.g. 'mongod &')\n##############################\n"
