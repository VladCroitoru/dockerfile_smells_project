FROM mrobson/base-openjdk:8

MAINTAINER Matthew Robson <matthewrobson@gmail.com>

RUN 	groupadd -r fuse -g 1000 && \
	useradd -u 1000 -r -g fuse -m -d /opt/fuse -s /sbin/nologin -c "Fuse User" fuse && \
	chmod 755 /opt/fuse && \
	echo "fuse hard nproc 65536" >> /etc/security/limits.conf && \
	echo "fuse soft nproc 65536" >> /etc/security/limits.conf && \
	echo "fuse hard nofile 65536" >> /etc/security/limits.conf && \
	echo "fuse soft nofile 65536" >> /etc/security/limits.conf

WORKDIR /opt/fuse

USER 1000
