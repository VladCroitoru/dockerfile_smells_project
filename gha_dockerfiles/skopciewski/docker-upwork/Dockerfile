FROM ubuntu:20.04

ENV CONTAINER_USER=user
ENV VERSION_URL https://upwork-usw2-desktopapp.upwork.com/binaries/v5_6_9_3_10c2eb9781db4d7f/upwork_5.6.9.3_amd64.deb

ADD $VERSION_URL /opt/upwork_amd64.deb
RUN apt-get update \
  && apt-get install -y sudo libx11-xcb1 libdrm2 libgbm1 \
  && dpkg -i /opt/upwork_amd64.deb || true \
  && apt-get install -f -y \
  && rm -rf /var/lib/apt/lists/*

COPY data/entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

ENTRYPOINT ["/sbin/entrypoint.sh"]
