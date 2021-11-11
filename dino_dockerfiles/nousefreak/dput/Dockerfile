FROM ubuntu

WORKDIR /app

RUN apt-get update \
	&& apt-get install -y \
		dput \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get clean

