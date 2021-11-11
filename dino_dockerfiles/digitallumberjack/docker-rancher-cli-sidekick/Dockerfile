FROM alpine:3.6
ARG RANCHER_VERSION=v0.6.2

RUN apk --no-cache add ca-certificates && update-ca-certificates
# RANCHER
RUN mkdir -p /opt/rancher/
ADD https://github.com/rancher/cli/releases/download/${RANCHER_VERSION}/rancher-linux-amd64-${RANCHER_VERSION}.tar.gz /usr/share/rancher-linux.tar.gz
RUN tar xvf /usr/share/rancher-linux.tar.gz --strip 2 -C /opt/rancher/
RUN chmod +x /opt/rancher/rancher
RUN ln -s /opt/rancher/rancher /usr/local/bin/rancher

VOLUME /opt/rancher
