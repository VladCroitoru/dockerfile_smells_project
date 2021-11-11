FROM		ubuntu:14.04
MAINTAINER	technopreneural@yahoo.com

VOLUME		["/var/cache/apt-cacher-ng"]

EXPOSE  	3142

#ENV		http_proxy http://acng.robin.dev:3142

RUN		apt-get update \
		&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
			apt-cacher-ng \
		&& rm -rf /var/lib/apt/lists/* \
		&& sed -i '/gentoo/s/^/#/' /etc/apt-cacher-ng/acng.conf

CMD     	chmod 777 /var/cache/apt-cacher-ng \
		&& /etc/init.d/apt-cacher-ng start \
		&& tail -f /var/log/apt-cacher-ng/*
