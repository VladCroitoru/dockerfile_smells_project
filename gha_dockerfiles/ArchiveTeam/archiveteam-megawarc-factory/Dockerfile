FROM debian:stretch-slim
RUN echo 'deb http://ftp.de.debian.org/debian buster-backports main' >> /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical apt-get -qqy --no-install-recommends -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-unsafe-io update \
 && DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical apt-get -qqy --no-install-recommends -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-unsafe-io install python python2.7 rsync git ca-certificates curl python-pip \
 && DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical apt-get -qqy --no-install-recommends -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold -o Dpkg::Options::=--force-unsafe-io -t buster-backports install zstd libzstd-dev libzstd1 \
 && pip install zstandard && pip install requests
COPY * factory/
RUN rm -rf /factory/megawarc && git clone https://github.com/archiveteam/megawarc.git /factory/megawarc
WORKDIR /factory
COPY docker-boot.sh /
RUN chmod +x /docker-boot.sh
ENTRYPOINT ["/docker-boot.sh"]
