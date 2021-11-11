FROM library/debian:wheezy
MAINTAINER Kenneth Peiruza <kenneth@floss.cat>
#    El canvi de nameserver només ens cal a l'Esteve Terradas :) 
RUN \
apt-get update && \
apt-get -y upgrade && \
apt-get -y install iputils-ping netcat-traditional && \
apt-get clean && \
apt-get autoclean && \
rm -rf /var/lib/apt/lists/* 
