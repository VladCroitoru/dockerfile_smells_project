FROM ubuntu:14.04
MAINTAINER heckenmann

ENV RSA_KEY_SIZE=4096

WORKDIR /etc
RUN mkdir letsencrypt
RUN mkdir letsencrypt/archive

WORKDIR /opt
RUN apt-get update && apt-get --yes dist-upgrade && apt-get --yes install wget git && apt-get --yes clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone https://github.com/letsencrypt/letsencrypt
WORKDIR /opt/letsencrypt

RUN chmod a+x ./certbot-auto
CMD ./certbot-auto certonly -a manual --rsa-key-size $RSA_KEY_SIZE -d $DOMAIN
