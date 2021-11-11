FROM debian:stretch-slim
MAINTAINER Jujhar Singh <jujhar@jujhar.com>

# Ignore APT warnings about not having a TTY
ENV DEBIAN_FRONTEND noninteractive

# Ensure UTF-8 locale
RUN echo "LANG=\"en_GB.UTF-8\"" > /etc/default/locale

RUN apt-get update \
	&& apt-get install -y \
    wget \
    imagemagick
	 
RUN apt-get clean autoclean \
	&& apt-get autoremove --yes \
	&& rm -rf /var/lib/{apt,dpkg,cache,log}/
