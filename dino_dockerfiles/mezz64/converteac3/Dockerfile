FROM ubuntu:latest

MAINTAINER mezz64 <jtmihalic@gmail.com>

ENV USER_ID=99
ENV GROUP_ID=100

# install packages
RUN apt-get update && \
    apt-get install -yq mkvtoolnix ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#make config folder
RUN \
 mkdir /config 

#Add start script
ADD start.sh /start.sh
RUN chmod +x /start.sh

#Add conversion script
ADD converteac3.sh /converteac3.sh
RUN chmod +x /converteac3.sh

VOLUME ["/config"]

WORKDIR /config

ENTRYPOINT ["/start.sh"]
