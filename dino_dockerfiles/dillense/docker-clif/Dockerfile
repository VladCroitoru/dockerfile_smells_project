FROM ubuntu:18.04

LABEL maintainer="bruno.dillenseger@orange.com"

ENV CLIF clif-2.3.8-server
ENV JAVA openjdk-8-jdk

RUN \
	apt-get update && \
	apt-get -y install vim wget unzip $JAVA iproute2 iputils-ping dnsutils net-tools && \
	wget -q http://clif.ow2.io/clif-legacy/download/$CLIF.zip -O /tmp/$CLIF.zip && \
	unzip -d /opt /tmp/$CLIF.zip
RUN \
	adduser --quiet --disabled-password --gecos "CLIF user" --shell /bin/bash clif && \
	echo "PATH=\"$PATH:/opt/$CLIF/bin\"" >> /home/clif/.profile
RUN \
	apt-get -y --purge autoremove && \
	apt-get -y clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 1234
EXPOSE 1357
ENTRYPOINT ["/bin/bash", "-l"]
