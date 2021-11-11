FROM ubuntu:16.04

ENV CLI_VERSION 2.3.0-6434-gd354690-0ubuntu1~16.04.1
ENV MAAS_KEYID 684D4A1C

RUN echo "deb http://ppa.launchpad.net/maas/stable/ubuntu xenial main" > /etc/apt/sources.list.d/maas-ubuntu-stable-xenial.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $MAAS_KEYID

RUN apt-get update -y \
	&& apt-get install -y --no-install-recommends \
		maas-cli=$CLI_VERSION \
	&& rm -rf /var/lib/apt/lists/*

ADD docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["maas-cli"]
