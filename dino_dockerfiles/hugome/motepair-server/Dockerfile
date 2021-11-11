FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y git nodejs npm

RUN mkdir -p /home/motepair-server
WORKDIR /home/motepair-server


RUN git clone git://github.com/motepair/motepair-server.git ./
RUN npm install

ADD run.sh run.sh

EXPOSE 3000
VOLUME /home/motepair-server/ssl

CMD /home/motepair-server/run.sh
