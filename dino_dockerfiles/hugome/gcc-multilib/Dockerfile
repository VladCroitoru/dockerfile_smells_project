FROM buildpack-deps:wily
MAINTAINER Hugome <hugo@hugome.eu>

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y \
	g++-multilib \
	gcc-multilib \
	libc6-dev-i386 \
	zlib1g-dev \
	zlib1g-dev:i386
RUN mkdir -p /out