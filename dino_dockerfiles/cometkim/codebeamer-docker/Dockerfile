FROM debian:jessie 

MAINTAINER Hyeseong Kim <hyeseong.kim@architectgroup.com>

RUN useradd -r codebeamer

RUN echo "deb http://ftp.debian.org/debian stretch main" > /etc/apt/sources.list.d/jessie-backports.list \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		cpio \
		openjdk-8-jdk \
		git \
		subversion \
		mercurial \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/codebeamer /opt/codebeamer
RUN chown codebeamer /usr/src/codebeamer /opt/codebeamer

RUN curl https://intland.com/wp-content/uploads/2017/03/CB-8.1.0-final-linux.bin > /tmp/CB-8.1.0-final-linux.bin
RUN chmod +x /tmp/CB-8.1.0-final-linux.bin
RUN { \
	echo "/usr/src/codebeamer/setup"; \
	echo "n"; \
} | su codebeamer -c /tmp/CB-8.1.0-final-linux.bin
RUN rm -rf /tmp/*

VOLUME ["/opt/codebeamer/repository", "/opt/codebeamer/tomcat/logs"]

COPY docker-entry.sh /
RUN chmod +x /docker-entry.sh
ENTRYPOINT ["/docker-entry.sh"]

WORKDIR /opt/codebeamer

EXPOSE 8080 8443
