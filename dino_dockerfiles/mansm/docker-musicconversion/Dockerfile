FROM debian:latest

MAINTAINER Mans Matulewicz <cybermans@gmail.com>

RUN apt-get update && \
	apt-get install -y flac libav-tools file && \
#	apt-get install -y git && \
	apt-get install -y autogen automake zlib1g-dev make unzip g++

ADD atomicparseley.zip /tmp/atomicparseley.zip
ADD atomicbuild.sh /tmp/atomicbuild.sh
ADD flac2alac.sh /root/flac2alac.sh
RUN chmod +x /tmp/atomicbuild.sh
RUN chmod +x /root/flac2alac.sh
RUN /tmp/atomicbuild.sh


RUN apt-get remove -y autogen automake zlib1g-dev make unzip g++
RUN apt-get -y autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/in"]
VOLUME ["/out"]


CMD ["/root/flac2alac.sh"]

#run --rm -t  --name musicconv -v /Users/Mans/Documents/projecten/docker/volumes/in:/in  -v /Users/mans/Documents/projecten/docker/volumes/out:/out -i musicconv /sbin/my_init -- bash -l