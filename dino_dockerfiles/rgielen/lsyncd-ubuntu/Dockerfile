FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends lsyncd rsync openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

ENTRYPOINT ["lsyncd", "-nodaemon"]
