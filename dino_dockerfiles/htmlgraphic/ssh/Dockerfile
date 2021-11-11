FROM ubuntu:16.04
MAINTAINER Jason Gegere <jason@htmlgraphic.com>

# Install packages then remove cache package list information
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -yq install \
		sudo \
		wget \
		zip \
		make \
		unzip \
		vim \
		curl \
		mailutils \
		dnsutils \
		language-pack-en \
		iputils-ping \
		openssh-client \
		openssh-server \
		git && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

ADD run.sh /run.sh
RUN chmod +x /*.sh

# Environment variables contained within build container.
ENV AUTHORIZED_KEYS=$AUTHORIZED_KEYS

EXPOSE 22
CMD ["/run.sh"]
