FROM ubuntu:focal-20211006
LABEL maintainer "fsdevops@evry.com"
#avoid interactive dialouges from apt:
ENV DEBIAN_FRONTEND=noninteractive LANG=C.UTF-8
RUN apt-get update && \
	apt-get --no-install-recommends -y install curl ca-certificates vim-tiny iputils-ping netcat net-tools tar gzip bzip2 unzip tzdata lsof psmisc less && \
	apt-get -y clean && \
	rm -rf /var/cache/apt /var/lib/apt/lists/* /tmp/* /var/tmp/*
