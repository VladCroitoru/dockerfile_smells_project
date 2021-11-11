FROM debian
MAINTAINER Gustavo Lichti <gustavo.lichti@tricae.com.br>

ENV DEBIAN_FRONTEND noninteractive

#Upgrade
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install openvpn -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#Set timezone America/Sao_Paulo
RUN echo 'America/Sao_Paulo' >/etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata


WORKDIR /etc/openvpn
