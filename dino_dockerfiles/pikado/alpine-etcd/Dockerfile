FROM alpine:latest
MAINTAINER Pika Do <pokido99@gmail.com>

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade system
RUN apk --no-cache upgrade

# Install various tools
RUN apk --no-cache add curl

# Install etcd2
ENV ETCD_VERSION 3.0.2
ENV ETCD_USER etcd
ENV ETCD_HOME /usr/local/etcd
RUN curl -sL https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-amd64.tar.gz | tar -xz -C /usr/local && \
    ln -s ${ETCD_HOME}* ${ETCD_HOME} && adduser -D -s /bin/sh ${ETCD_USER} && chown -R ${ETCD_USER}: ${ETCD_HOME}*
USER $ETCD_USER
ADD run.sh /
EXPOSE 2379 2380

# Define default command
CMD /run.sh 
