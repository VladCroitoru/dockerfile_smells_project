FROM debian:stretch
LABEL MAINTAINER="Sylvain Lamontagne <sylvain.lamontagne@gmail.com>"

ENV RCLONE_VERSION=current
ENV ARCH=amd64

RUN apt-get update && \
    apt-get --no-install-recommends install -y wget ca-certificates fuse cron gawk unzip && \
    apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
      && wget -q http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \
      && unzip /tmp/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \
      && mv /tmp/rclone-*-linux-${ARCH}/rclone /usr/bin \
      && rm -r /tmp/rclone*


ADD start.sh /usr/bin/start.sh
RUN chmod +x /usr/bin/start.sh
ADD sync.sh /usr/bin/sync.sh
RUN chmod +x /usr/bin/sync.sh

RUN mkdir -p /root/.config/rclone

ENTRYPOINT ["/usr/bin/start.sh"]
CMD [""]
