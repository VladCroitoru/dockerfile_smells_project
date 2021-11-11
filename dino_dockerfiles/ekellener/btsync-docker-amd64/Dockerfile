FROM ubuntu:14.04
MAINTAINER Erik Kellener (erik@kellener.com)

ENV DEBIAN_FRONTEND noninteractive

########## BTSYNC ##########

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install curl -y
RUN apt-get install jq -y

RUN curl -o /usr/bin/btsync.tar.gz  https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz
RUN cd /usr/bin; tar xvzf btsync.tar.gz; rm btsync.tar.gz;
RUN ln -s /usr/bin/rslsync /usr/bin/btsync

WORKDIR /btsync


ADD run_btsync.sh run_btsync.sh
ADD config.json config.json
ADD config.json config.default.json
RUN mkdir /btsync/storage

EXPOSE 55555


# Arguments: DIR SECRET
ENTRYPOINT ["/bin/bash", "run_btsync.sh"]
