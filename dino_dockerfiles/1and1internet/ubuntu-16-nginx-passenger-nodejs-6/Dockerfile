FROM 1and1internet/ubuntu-16-nginx-passenger
MAINTAINER brian.wilkinson@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
RUN \
	apt-get update -q && \
	apt-get install -y curl apt-transport-https ca-certificates lsb-release && \
	DISTRO=$(lsb_release -c -s) && \
	NODEREPO="node_6.x" && \
	curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
	echo "deb https://deb.nodesource.com/${NODEREPO} ${DISTRO} main" > /etc/apt/sources.list.d/nodesource.list && \
	echo "deb-src https://deb.nodesource.com/${NODEREPO} ${DISTRO} main" >> /etc/apt/sources.list.d/nodesource.list && \
	apt-get update -q && \
	apt-get install -y build-essential nodejs && \
	sed -i 's|wsgi;|node;\n        passenger_startup_file app.js;|' /etc/nginx/sites-enabled/default && \
	/usr/bin/passenger-config validate-install  --auto --no-colors && \
	apt-get -y clean && \
	rm -rf /var/lib/apt/lists/*
