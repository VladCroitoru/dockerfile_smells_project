FROM ubuntu:xenial
MAINTAINER Willy Ko <wko@blockchainfoundry.co>

ARG USER_ID
ARG GROUP_ID

ENV HOME /syscoin

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -g ${GROUP_ID} syscoin \
	&& useradd -u ${USER_ID} -g syscoin -s /bin/bash -m -d /syscoin syscoin

ENV SYSCOIN_VERSION 4.1.2.1
RUN set -x \ 
        && apt-get update \
        && apt-get install -y wget ca-certificates \
        && wget "https://github.com/syscoin/syscoin/releases/download/v$SYSCOIN_VERSION/syscoin-$SYSCOIN_VERSION-x86_64-linux-gnu.tar.gz"  \
        && wget "https://github.com/syscoin/syscoin/releases/download/v$SYSCOIN_VERSION/SHA256SUMS.asc" \
        && export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 79D00BAC68B56D422F945A8F8E3A8F3247DBCBBF \
	&& gpg --verify SHA256SUMS.asc \
        && sha256sum --ignore-missing --check SHA256SUMS.asc \
        && tar xf syscoin-$SYSCOIN_VERSION-x86_64-linux-gnu.tar.gz \
        && install -m 0755 -o root -g root -t /usr/local/bin syscoin-$SYSCOIN_VERSION/bin/* \
        && rm -r "$GNUPGHOME" "syscoin-$SYSCOIN_VERSION" "syscoin-$SYSCOIN_VERSION-x86_64-linux-gnu.tar.gz" \
	&& apt-get purge -y \
		ca-certificates \
		wget \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		wget \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y \
		ca-certificates \
		wget \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./bin /usr/local/bin

VOLUME ["/syscoin"]

EXPOSE 8369 8370 18369 18370 30303

WORKDIR /syscoin

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["sys_oneshot"]
