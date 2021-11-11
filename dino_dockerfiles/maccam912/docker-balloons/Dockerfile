FROM ubuntu:trusty
MAINTAINER Matt Koski <maccam912@gmail.com>

RUN apt-get update ; apt-get upgrade -y

RUN apt-get install wget vim build-essential git python curl -y

RUN mkdir /Development
RUN cd /Development ; git clone git://github.com/joyent/node

RUN cd /Development/node ; ./configure ; make ; make install
RUN rm -rf /Development/node
RUN chmod 777 -R /Development

RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh ; sh spf13-vim.sh

RUN wget http://redis.googlecode.com/files/redis-2.4.17.tar.gz ; tar xvf redis-2.4.17.tar.gz ; cd redis-2.4.17 ; make ; make install

RUN git clone https://github.com/gravityonmars/Balloons.IO.git ; cd Balloons.IO ; npm install ; mv config/config.sample.json config/config.json
