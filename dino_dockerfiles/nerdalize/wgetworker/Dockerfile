FROM ubuntu:16.04

RUN apt-get update \
	&& apt-get install -y \
		vim \
		curl \
		wget \
	&& rm -rf /var/lib/apt/lists/*

COPY run.sh /run.sh
ENTRYPOINT ["./run.sh"]
