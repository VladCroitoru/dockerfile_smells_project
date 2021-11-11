FROM debian:latest

MAINTAINER Mans Matulewicz <cybermans@gmail.com>
LABEL usage="spl () { docker run --rm -v $1:/root albumsplitter; }"

RUN apt-get update && \
	apt-get install -y wget 

RUN wget https://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-multimedia-keyring_2015.6.1_all.deb
RUN dpkg -i deb-multimedia-keyring_2015.6.1_all.deb

RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN apt-get update && \
	apt-get install -y shntool flac monkeys-audio libmac2 cuetools

ADD converter.sh /opt/converter.sh
RUN chmod +x /opt/converter.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /root
ENV FILEEXT ape
CMD /opt/converter.sh $FILEEXT