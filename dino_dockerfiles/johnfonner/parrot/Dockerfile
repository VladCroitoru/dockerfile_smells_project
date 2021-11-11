# FROM taccsciapps/base:latest
FROM gliderlabs/alpine 
RUN apk-install bash

MAINTAINER John Fonner <jfonner@tacc.utexas.edu>

WORKDIR /

COPY project/parrot.sh /tmp/parrot.sh
COPY project/header.txt /tmp/header.txt
COPY data/example.txt /tmp/example.txt

ENV PATH /tmp:$PATH
