FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y git python default-jre wget unzip build-essential libz-dev ncbi-blast+ libidn11 r-base
RUN git clone https://github.com/mrmckain/fast-plast.git
RUN cd /fast-plast && echo -e "n\nall" | perl INSTALL.pl
VOLUME /data
WORKDIR /data
