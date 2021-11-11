FROM ubuntu:wily
MAINTAINER caktux

ENV DEBIAN_FRONTEND noninteractive

# Usual update / upgrade
RUN apt-get update \
	&& apt-get upgrade -q -y \
	&& apt-get dist-upgrade -q -y \
	&& apt-get install -q -y software-properties-common \
	&& add-apt-repository -y ppa:ethereum/ethereum-qt \
	&& add-apt-repository -y ppa:ethereum/ethereum \
	&& add-apt-repository -y ppa:ethereum/ethereum-dev \
	&& apt-get update \
	&& apt-get install -q -y ethereum geth

EXPOSE 8545
EXPOSE 30303

ENV HOME /home/ethereum/

WORKDIR ${HOME}

RUN groupadd -r ethereum \
	&& useradd -r -g ethereum ethereum \
	&& chown -R ethereum ${HOME}

USER ethereum
