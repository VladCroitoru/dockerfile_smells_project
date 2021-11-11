FROM kalledk/debian:jessie

MAINTAINER Kalle R. Møller <docker-doxygen@k-moeller.dk>

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
		doxygen \
		graphviz \
	&& rm -rf /var/lib/apt/lists/*

VOLUME ["/data/src", "/data/output"]

WORKDIR /data/src

ADD entry.sh /entry.sh

ENTRYPOINT ["/entry.sh"]
