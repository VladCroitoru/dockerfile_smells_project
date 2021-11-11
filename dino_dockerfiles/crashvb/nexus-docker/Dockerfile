FROM crashvb/supervisord:latest
MAINTAINER Richard Davis <crashvb@gmail.com>

# Install packages, download files ...
ENV NEXUS_DATA=/var/lib/nexus NEXUS_HOME=/usr/share/nexus NEXUS_VERSION=3.3.1-01
RUN docker-apt default-jdk-headless && \
	mkdir --parents ${NEXUS_DATA} ${NEXUS_HOME} && \
	wget --quiet --output-document=- https://download.sonatype.com/nexus/3/nexus-$NEXUS_VERSION-unix.tar.gz | \
	tar --directory=${NEXUS_HOME} --extract --gzip --strip-components=1 nexus-${NEXUS_VERSION} && \
	ln --symbolic ${NEXUS_DATA} /usr/share/sonatype-work

# Configure: nexus
RUN useradd --comment="Nexus Daemon" --home=${NEXUS_HOME} --shell=/bin/bash nexus && \
	chown --recursive nexus:nexus ${NEXUS_HOME}

# Configure: supervisor
ADD supervisord.nexus.conf /etc/supervisor/conf.d/nexus.conf

# Configure: entrypoint
ADD entrypoint.nexus /etc/entrypoint.d/10nexus

EXPOSE 5000/tcp 8081/tcp

VOLUME ${NEXUS_DATA}
