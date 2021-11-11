FROM ubuntu:bionic
LABEL maintainer="Evgeniy Slizevich <evgeniy@slizevich.net>"

WORKDIR /
RUN apt-get update && apt-get install -y wget gawk && rm -rf /var/lib/apt/lists/*
RUN wget -qO - `wget -qO - https://repo-feed.flightradar24.com/fr24feed_versions.json | grep -Eo 'http://.*?/linux_x86_64_binaries/fr24feed_.*?_amd64.tgz'` | tar xzf -

ADD fr24feed /fr24feed

EXPOSE 8754

ENTRYPOINT ["/fr24feed"]
