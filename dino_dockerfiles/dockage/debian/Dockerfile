FROM debian:jessie-slim
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gamil.com>

ENV GOSU_VERSION 1.10
ENV DEBIAN_FRONTEND noninteractive

RUN echo 'APT::Install-Recommends 0;\nAPT::Install-Suggests 0;' > /etc/apt/apt.conf.d/01norecommends \
    && echo 'APT::Get::Assume-Yes "true";\nAPT::Get::force-yes "true";' > /etc/apt/apt.conf.d/01buildconfig \
    #&& echo 'Package: systemd\nPin: release *\nPin-Priority: -1' > /etc/apt/preferences.d/systemd \
    #&& echo '\n\nPackage: *systemd*\nPin: release *\nPin-Priority: -1' >> /etc/apt/preferences.d/systemd \
    #&& echo '\nPackage: systemd:amd64\nPin: release *\nPin-Priority: -1' >> /etc/apt/preferences.d/systemd \
    #&& echo '\nPackage: systemd:i386\nPin: release *\nPin-Priority: -1' >> /etc/apt/preferences.d/systemd \
    && apt-get update \
    #&& apt-get -y --force-yes -qq remove --purge --auto-remove systemd \
    && apt-get install -y vim.tiny wget sudo net-tools ca-certificates unzip apt-transport-https software-properties-common \
    #&& rm -rf /etc/systemd /lib/systemd /lib/x86_64-linux-gnu/libsystemd* /usr/share/doc/libsystemd0 /var/lib/dpkg/info/libsystemd0:* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    # Installing gosu
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true
