FROM debian:jessie
ENV VERSION=v0.2.0
ADD https://github.com/jwilder/docker-squash/releases/download/$VERSION/docker-squash-linux-amd64-$VERSION.tar.gz /root/docker-squash-linux-amd64-$VERSION.tar.gz
RUN tar -C /usr/local/bin -xvzf /root/docker-squash-linux-amd64-$VERSION.tar.gz

RUN apt-get update && apt-get install -y sudo

ENTRYPOINT ["docker-squash"]
