FROM ubuntu:latest
LABEL maintainer "infiniteproject@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install \
        software-properties-common && \
    add-apt-repository ppa:duplicity-team/ppa

RUN apt-get update && apt-get -y install \
	duplicity \
        lftp \
	python-pip && \
    pip install dropbox
	
RUN apt-get clean && \
    rm -fr /var/lib/apt/lists/* \
        /tmp/* \
	/var/tmp/*
	
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
