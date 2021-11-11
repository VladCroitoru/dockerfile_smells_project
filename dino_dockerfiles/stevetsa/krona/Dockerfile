# This is a comment

FROM ubuntu:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>
RUN apt-get update

RUN apt-get install --yes \
 build-essential \
 wget \
 curl

ENV DEBIAN_FRONTEND=noninteractive
RUN wget https://github.com/marbl/Krona/releases/download/v2.7/KronaTools-2.7.tar
RUN tar -xvf KronaTools-2.7.tar
WORKDIR KronaTools-2.7
RUN ./install.pl
#RUN ./updateAccessions.sh
#RUN ./updateTaxonomy.sh
WORKDIR /
