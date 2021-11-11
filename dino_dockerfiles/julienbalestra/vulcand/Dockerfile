FROM debian:latest

WORKDIR /tmp

ENV VERSION=https://github.com/vulcand/vulcand/releases/download/v0.8.0-beta.3/vulcand-v0.8.0-beta.3-linux-amd64.tar.gz

RUN apt-get update && \
apt-get upgrade -y && \
DEBIAN_FRONTEND=noninteractive apt-get install curl -y && \
curl -LO $VERSION && \
tar -xzvf vulcand* && \
mv vulcand*/vulcand /usr/sbin/vulcand && \
rm -rf /tmp/* && \
apt-get clean autoclean && \
apt-get autoremove -y

ENTRYPOINT ["/usr/sbin/vulcand"]

