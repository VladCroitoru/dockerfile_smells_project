FROM 1and1internet/ubuntu-16-nginx-passenger
MAINTAINER brian.wilkinson@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive

ENV VIRTENV /var/www/._venv
ENV VIRTUAL_ENV_DISABLE_PROMPT true
ENV PATH $VIRTENV/bin:$PATH

COPY files /

RUN \
	apt-get update -q && \
	apt-get install -q -o Dpkg::Options::=--force-confdef -y virtualenv python3-venv python3-virtualenv python3-all python3-setuptools python3-pip && \
	apt-get install -q -o Dpkg::Options::=--force-confdef -y python-dev python3-dev python-pip && \
	pip install requests logging && \
	echo "passenger_python ${VIRTENV}/bin/python3;" >> /etc/nginx/passenger.conf && \
	/usr/bin/passenger-config validate-install  --auto --no-colors && \
	apt-get -y clean && \
	rm -rf /var/lib/apt/lists/*

EXPOSE 8080 8443
WORKDIR /var/www

