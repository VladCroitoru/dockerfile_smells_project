FROM debian:unstable

ENV DEBIAN_FRONTEND=noninteractive

# update the package repositories
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y wget curl locales

# Configure timezone and locale
RUN echo "Europe/Stockholm" > /etc/timezone && \
	dpkg-reconfigure -f noninteractive tzdata
RUN export LANGUAGE=en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	export LC_ALL=en_US.UTF-8 && \
	locale-gen en_US.UTF-8 && \
	dpkg-reconfigure locales

# install zulucrypt dependencies
RUN apt-get update && \
	apt-get install --allow-unauthenticated -y libblkid-dev libqt4-dev gcc g++ \
	libcryptsetup-dev cmake libgcrypt11-dev pkg-config libdevmapper-dev \
	clang
