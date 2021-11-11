FROM debian

LABEL "de.andrelademann"="André Lademann" \
	version="0.0.4" \
	description="Docker debian image to use for development, testing and deployment."

COPY setup/ /

RUN apt-get update &&\
		apt-get install -y \
		bash \
		bash-completion \
		bats \
		bzip2 \
		ca-certificates \
		curl \
		figlet \
		findutils \
		git \
		locales \
		make \
		mc \
		powerline \
		siege \
		wget \
		vim \
		zip

RUN locale-gen en_GB.UTF-8

ENV	POWERLINE_BASH_CONTINUATION=1 \
		POWERLINE_BASH_SELECT=1
