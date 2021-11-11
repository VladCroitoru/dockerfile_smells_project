FROM ubuntu:15.10

# Add PPA repositories
RUN echo deb http://ppa.launchpad.net/ethereum/ethereum/ubuntu wily main >> /etc/apt/sources.list
RUN echo deb http://ppa.launchpad.net/ethereum/ethereum-dev/ubuntu wily main >> /etc/apt/sources.list
RUN echo deb http://ppa.launchpad.net/ethereum/ethereum-qt/ubuntu wily main >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 923F6CA9

RUN apt-get update && apt-get -y --no-install-recommends install mix solc

RUN adduser --disabled-password --gecos "" mixuser
USER mixuser

