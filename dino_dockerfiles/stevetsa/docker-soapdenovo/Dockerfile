FROM ubuntu:14.04
RUN \
apt-get update && apt-get install -y \
wget \
make \
automake \
g++ \
gcc \
zlib1g-dev

ENV SRC /opt
ENV BIN /usr/local/bin

WORKDIR $SRC
RUN wget https://github.com/aquaskyline/SOAPdenovo2/archive/r241.tar.gz && \
	tar -xvf r241.tar.gz && \
	cd SOAPdenovo2-r241/ && \
	make && \
	cp -rf  *  $BIN


COPY Dockerfile /opt/Dockerfile


