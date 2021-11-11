FROM 1and1internet/ubuntu-16-nginx-passenger
MAINTAINER brian.wilkinson@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive

ENV VIRTENV /var/www/._venv
ENV VIRTUAL_ENV_DISABLE_PROMPT true
ENV PATH $VIRTENV/bin:$PATH

COPY files /

RUN \
	apt-get update -q && \
	apt-get install -q -o Dpkg::Options::=--force-confdef -y python-dev && \
	apt-get remove python-pip python3-pip && \
	wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && \
	/usr/bin/python2.7 get-pip.py && \
	rm -f get-pip.py && \
	pip install --no-cache-dir --upgrade requests logging virtualenv && \
	echo "passenger_python ${VIRTENV}/bin/python;" >> /etc/nginx/passenger.conf && \
	/usr/bin/passenger-config validate-install  --auto --no-colors && \
	apt-get -y clean && \
	rm -rf /var/lib/apt/lists/* && \
	mkdir /.cache && chmod 777 /.cache

EXPOSE 8080 8443
WORKDIR /var/www
