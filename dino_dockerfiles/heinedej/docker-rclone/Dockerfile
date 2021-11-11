FROM bitnami/minideb:jessie
MAINTAINER heine <heinedej@gmail.com>

# global environment settings
ENV RCLONE_VERSION="current"
ENV RCLONE_ARCH="amd64"

# install packages
RUN \
 install_packages wget unzip ca-certificates && \
 
 cd tmp && \
 wget -q http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${RCLONE_ARCH}.zip && \
 unzip /tmp/rclone-${RCLONE_VERSION}-linux-${RCLONE_ARCH}.zip && \
 mv /tmp/rclone-*-linux-${RCLONE_ARCH}/rclone /usr/local/bin && \
 
# cleanup
 rm -rf \
	/tmp/* \
	/var/tmp/*

ENTRYPOINT ["/usr/local/bin/rclone"]

VOLUME ["/config"]

CMD ["--version"]
