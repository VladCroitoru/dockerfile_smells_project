FROM ubuntu:14.04
MAINTAINER al@albush.com

# Install PREREQS 
RUN apt-get -qq update
RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends locales build-essential python-dev python-pip git-core python-pygments
RUN rm -rf /var/lib/apt/lists/*
	
# Fix locale
RUN locale-gen en_US.UTF-8

# Download and install hugo
ENV HUGO_VERSION 0.12
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64

ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/local/
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \
	&& ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \
	&& rm /usr/local/${HUGO_BINARY}.tar.gz

# Create working directory
RUN mkdir /usr/share/blog
WORKDIR /usr/share/blog
