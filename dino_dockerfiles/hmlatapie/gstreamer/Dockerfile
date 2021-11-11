FROM ubuntu:15.10

RUN apt-get update && \
	apt-get upgrade -y && \
 	apt-get install -y gstreamer-1.0* && \
 	apt-get install -y gstreamer1.0* && \
 	apt-get install -y aptitude && \
 	cpan Data::Dumper && \
	apt-get install -y vim && \
	apt-get install -y ffmpeg	&& \
	apt-get install -y imagemagick

VOLUME /root/images 
WORKDIR /root/images

