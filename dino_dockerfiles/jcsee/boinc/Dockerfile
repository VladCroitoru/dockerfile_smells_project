FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive \
    VERSION=7.9.3+dfsg-5ubuntu2

RUN apt-get update \
 && apt-get install --assume-yes --no-install-recommends \
      boinc=$VERSION \
      boinctui \
      ca-certificates \
      net-tools \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]
