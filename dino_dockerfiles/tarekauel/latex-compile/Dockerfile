FROM debian:jessie
MAINTAINER Tarek Auel <tarek@auel.io>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q
RUN apt-get install -qy texlive-full 
RUN apt-get install -qy python-pygments 
RUN apt-get install -qy gnuplot

COPY texmf /usr/share/texmf

RUN texhash

RUN updmap-sys --enable Map 5ch.map && \
updmap-sys --enable Map 5fp.map && \
updmap-sys --enable Map 5sf.map

WORKDIR /data
VOLUME ["/data"]
