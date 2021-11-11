FROM openjdk:8
MAINTAINER Christian Winther <cw@bownty.com>

ENV RUNDECK_VERSION 2.7.1-1
ENV GOSU_VERSION=1.10

RUN set -ex \
	# install go-su ( https://github.com/tianon/gosu )
	&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
	&& wget -q -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
	&& wget -q -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \

    && wget -q http://dl.bintray.com/rundeck/rundeck-deb/rundeck-${RUNDECK_VERSION}-GA.deb \
    && dpkg -i rundeck-${RUNDECK_VERSION}-GA.deb \
    && rm rundeck-${RUNDECK_VERSION}-GA.deb \

    && mkdir -p /var/lib/rundeck/contrib-plugins/

COPY ["bin/rundeck-boot", "/usr/local/bin"]

VOLUME ["/var/lib/rundeck/logs", "/etc/rundeck", "/var/rundeck/projects", "/var/log/rundeck/", "/var/lib/rundeck/contrib-plugins"]

CMD "rundeck-boot"

