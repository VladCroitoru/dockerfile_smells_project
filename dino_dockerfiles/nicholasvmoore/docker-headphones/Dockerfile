# Headphones
#
# Version 0.0.1

FROM fedora:20
MAINTAINER Nicholas Moore

VOLUME /config
VOLUME /media

RUN yum -y install git; yum clean all;\
    cp -f /usr/share/zoneinfo/US/Pacific /etc/localtime;\
    git clone https://github.com/rembo10/headphones.git /opt

EXPOSE 8181

ENTRYPOINT ["/usr/bin/python", "/opt/Headphones.py", "--datadir=/config"]