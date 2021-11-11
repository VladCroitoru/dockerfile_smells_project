FROM ubuntu:16.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      weechat \
      weechat-scripts \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]
