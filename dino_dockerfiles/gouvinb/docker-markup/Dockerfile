FROM debian:latest

MAINTAINER gouvinb

LABEL "com.gouvinb.docker-markup"="gouvinb" \
      version="1.0"                         \
      description="A Docker image for markup tools, command Line Interface for markup tools."

RUN sed -i "s/stretch main/stretch main contrib non-free/" /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-full
RUN apt-get install -y biber
RUN apt-get install -y texlive-bibtex-extra
RUN apt-get install -y msttcorefonts
RUN apt-get clean
RUN mkdir /data

WORKDIR /data
