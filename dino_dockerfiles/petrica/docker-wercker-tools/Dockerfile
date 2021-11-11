FROM ubuntu:16.04

RUN apt-get -qqy update \
	&& apt-get -qqy --no-install-recommends install \
	software-properties-common \
	python-software-properties \
	jq \
	openssh-client \
	curl \
	bzip2 \
	unzip \
	wget \
	git \
	nano \
	ruby-full && \
	rm -rf /var/lib/apt/lists/* /var/cache/apt/*
