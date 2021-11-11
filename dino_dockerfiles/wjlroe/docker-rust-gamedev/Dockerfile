FROM wjlroe/docker-ubuntu-rust:latest
MAINTAINER William Roe "git@wjlr.org.uk"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
	apt-get install \
	uuid-dev \
	libssl-dev \
	libsdl2-dev \
	libsdl2-gfx-dev \
	libsdl2-image-dev \
	libsdl2-mixer-dev \
	libsdl2-net-dev \
	libsdl2-ttf-dev \
	libfreetype6-dev \
	tk-dev \
	-qqy \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives

ENV LAST_RUST_IMAGE_UPDATE=2018-10-13

RUN rustc --version
