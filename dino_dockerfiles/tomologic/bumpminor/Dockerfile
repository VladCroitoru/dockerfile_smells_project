FROM debian:wheezy

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

ADD bin/bumpminor /usr/bin/
ADD bin/semver /usr/bin/

RUN mkdir -p /app
WORKDIR /app

ENTRYPOINT [ "bumpminor" ]
