FROM golang:latest
MAINTAINER YAMASAKI Masahide <masahide.y@gmail.com>

RUN echo "deb http://http.debian.net/debian stretch-backports main contrib non-free" | tee /etc/apt/sources.list.d/stretch-backports.list \
    && apt-get update && apt-get install -y --no-install-recommends \
		jq bash openssh-client tar unzip wget clang \
    && apt-get install -t stretch-backports -y --no-install-recommends git \
	&& rm -rf /var/lib/apt/lists/*
