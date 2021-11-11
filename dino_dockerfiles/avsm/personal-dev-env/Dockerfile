FROM ubuntu:wily
MAINTAINER Anil Madhavapeddy <anil@recoil.org>
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install build-essential vim git libssl-dev
RUN useradd -ms /bin/bash -u 501 -g 20 avsm
USER avsm
WORKDIR /home/avsm
COPY .gitconfig /home/avsm/.gitconfig
