FROM debian:stable
ENV VERSION 2.2.7
MAINTAINER Ben Gibbons <axemann@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y btrfs-tools apt-utils sqlite3 libcrypto++-dev libcurl3 libfuse2 && apt-get clean && rm -rf /var/lib/apt/lists/*
ADD https://www.urbackup.org/downloads/Server/${VERSION}/debian/stretch/urbackup-server_${VERSION}_amd64.deb /root/install.deb
RUN echo /backup | dpkg -i /root/install.deb && rm /root/install.deb

EXPOSE 55413/tcp 55414/tcp 55415/tcp 35623/udp

VOLUME [ "/backup", "/var/urbackup", "/var/log", "/usr/share/urbackup" ]
ENTRYPOINT ["/usr/bin/urbackupsrv"]
CMD ["run"]
