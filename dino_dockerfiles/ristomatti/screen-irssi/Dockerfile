FROM debian:jessie

MAINTAINER Ristomatti Airo <ristomatti.airo@gmail.com>

RUN apt-get update && \
	apt-get install -y locales && \
	dpkg-reconfigure locales && \
	locale-gen C.UTF-8 en_US.UTF-8 fi_FI.UTF-8 && \
	/usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

RUN apt-get install -y openssh-server oidentd supervisor irssi screen \
		libgnutls-openssl27 && \
	apt-get clean

RUN mkdir -p /var/run/sshd /etc/supervisor/conf.d

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY irssi.conf /etc/irssi.conf

VOLUME ["/home"]

EXPOSE 22/tcp 113/tcp 

CMD ["/usr/bin/supervisord"]
