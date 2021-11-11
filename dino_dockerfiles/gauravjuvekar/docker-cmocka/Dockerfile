FROM ubuntu:latest
MAINTAINER Gaurav Juvekar <gauravjuvekar@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
		python3 \
		python3-pip \
		binutils \
		git \
		scons \
		build-essential \
		pkg-config \
		valgrind \
		gcovr \
		libcmocka0 \
		libcmocka-dev \
		&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip3 install numpy
