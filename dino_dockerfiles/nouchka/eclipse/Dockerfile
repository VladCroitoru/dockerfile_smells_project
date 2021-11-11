ARG  BASE_IMAGE=debian:jessie
FROM ${BASE_IMAGE}
MAINTAINER Jean-Avit Promis "docker@katagena.com"

ARG ECLIPSE_TAR_URL=http://ftp.fau.de/eclipse/technology/epp/downloads/release/mars/2/eclipse-php-mars-2-linux-gtk-x86_64.tar.gz
ARG ECLIPSE_VERSION=mars
ARG PUID=1000
ARG PGID=1000
ARG BASE_IMAGE=debian:jessie
LABEL version="${DOCKER_TAG}"

ENV PUID ${PUID}
ENV PGID ${PGID}
ENV ECLIPSE_VERSION ${ECLIPSE_VERSION}

##TODO remove curl or wget
##wget && curl to DL
##jdk for eclipse
##php php-cli php-xdebug for php dev
##git or svn for team
##libcanberra-gtk3-module for graph

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq install wget git subversion libcanberra-gtk3-module curl lintian fakeroot ssh-askpass openssh-client rsync python unzip && \
	[ "$BASE_IMAGE" != "ubuntu:xenial" ] || apt-get -yq install openjdk-8-jdk php7.0 php-cli php-xdebug php-intl php-xml && \
	[ "$BASE_IMAGE" != "debian:jessie" ] || apt-get -yq install openjdk-7-jdk php5 php5-cli php5-xdebug && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	wget ${ECLIPSE_TAR_URL} -O /tmp/eclipse.tar.gz -q && \
	tar -xf /tmp/eclipse.tar.gz -C /opt && \
	rm /tmp/eclipse.tar.gz && \
	wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer && \
	chmod a+x php-cs-fixer && \
	mv php-cs-fixer /usr/local/bin/php-cs-fixer && \
	curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
	php /usr/local/bin/composer self-update && \
	export uid=${PUID} gid=${PGID} && \
	mkdir -p /home/developer && \
	echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
	echo "developer:x:${uid}:" >> /etc/group && \
	chown ${uid}:${gid} -R /home/developer

COPY home/.wakatime.cfg /home/developer/.wakatime.cfg
COPY configuration/ /opt/eclipse/configuration/
COPY metadata/ /home/developer/metadata/

COPY launch.sh /launch.sh
RUN chmod +x /launch.sh && \
	chown developer: /launch.sh && \
	chown -R developer: /home/developer/.wakatime.cfg && \
	chown -R developer: /opt/eclipse/&& \
	chown -R developer: /home/developer/metadata/

USER developer
ENV HOME /home/developer

CMD /launch.sh
