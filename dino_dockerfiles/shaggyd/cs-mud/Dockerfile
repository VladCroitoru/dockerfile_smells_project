FROM ubuntu:14.04
MAINTAINER Dustin Chadwick <me@dchadwick.com>

RUN apt-get update && apt-get install -y \
  #build-essential \ 
  gcc \ 
  make \
  unzip \
  wget \
  csh && \
  apt-get clean

#RUN mkdir /cs-mud

#WORKDIR /cs-mud

RUN wget https://github.com/blakepell/CrimsonSkies/archive/master.zip
run unzip master.zip

WORKDIR /CrimsonSkies-master/area
RUN cd ../src && make

VOLUME [ "/opt/rom" ]
EXPOSE 4000

ENTRYPOINT [ "./startup" ]
