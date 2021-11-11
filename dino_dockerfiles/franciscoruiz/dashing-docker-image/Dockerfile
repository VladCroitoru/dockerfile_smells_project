FROM debian:jessie

MAINTAINER Francisco Ruiz <quiesagua@gmail.com>


RUN apt-get update \
	&& apt-get install --assume-yes --no-install-recommends \
		build-essential \
		ruby-full \
		zlib1g-dev \
		nodejs \
		ca-certificates \
	&& rm -rf /var/lib/apt/lists/* \
	&& gem install bundle dashing

EXPOSE 3030
