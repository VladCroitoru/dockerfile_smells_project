FROM ubuntu

MAINTAINER Elton Schivei Costa <costa@elton.schivei.nom.br>

RUN apt-get update && apt-get install --no-install-recommends -y rlwrap sqlite socat spatialite-bin \
&& rm -rf /var/lib/apt/lists/* 

EXPOSE 7022
