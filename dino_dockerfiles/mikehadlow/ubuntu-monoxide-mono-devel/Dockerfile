#DOCKER-VERSION 0.9.1
#
#VERSION 0.1
#
# monoxide mono-devel package on Ubuntu 13.10

FROM    ubuntu:13.10
MAINTAINER Mike Hadlow <mike@suteki.co.uk>

RUN     sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q software-properties-common
RUN     sudo add-apt-repository ppa:directhex/monoxide -y
RUN     sudo apt-get update
RUN     sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q mono-devel
