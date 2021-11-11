FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y software-properties-common && apt-get install -y octave && apt-get remove -y software-properties-common

RUN apt-get autoclean && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && mkdir /source
	
ADD . /source/
WORKDIR /source

VOLUME ["/source"]
ENTRYPOINT ["octave"]
