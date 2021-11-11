# kentwait/docker-openmpi
FROM phusion/baseimage:latest

# Container metadata
LABEL version="2.0"
LABEL maintainer="Kent Kawashima <kentkawashima@gmail.com>"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
USER root

RUN apt-get update --quiet --fix-missing && \
	# Install dependencies
	apt-get install -y \
		build-essential \
		wget \	
		curl \
		bzip2 \
		grep \
		sed \
		dpkg \
		git \
		python-dev \
		python3-dev \
		ca-certificates \
		gfortran && \
	# Install OpenMPI		
	apt-get install -y \
		libopenmpi-dev \
		openmpi-bin && \
	apt-get clean && \
 	rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/sbin/my_init"]