FROM resin/armv7hf-debian-qemu

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -qq -y \
	build-essential \
	patch \
	ruby \
	ruby-dev \
	zlib1g-dev \
	liblzma-dev \
	bash \
	cron \
 	vim \
&& rm -rf /var/lib/apt/lists/*

RUN [ "cross-build-end" ]
