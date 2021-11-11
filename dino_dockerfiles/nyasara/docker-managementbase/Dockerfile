FROM ubuntu:latest

# Install confd and etcdctl
RUN apt-get update \
    && apt-get -yq install wget git curl python \
    &&  wget https://github.com/kelseyhightower/confd/releases/download/v0.6.3/confd-0.6.3-linux-amd64 \
    && mv confd-0.6.3-linux-amd64 /usr/local/bin/confd \
    && chmod +x /usr/local/bin/confd \
    && curl -L  https://github.com/coreos/etcd/releases/download/v0.5.0-alpha.4/etcd-v0.5.0-alpha.4-linux-amd64.tar.gz -o etcd-v0.5.0-alpha.4-linux-amd64.tar.gz \
    && tar xzvf etcd-v0.5.0-alpha.4-linux-amd64.tar.gz \
    && mv etcd-v0.5.0-alpha.4-linux-amd64/etcdctl /usr/local/bin/etcdctl \
    && chmod +x /usr/local/bin/etcdctl \
    && mkdir /etc/confd \
    && mkdir /etc/confd/conf.d \
    && mkdir /etc/confd/templates \
    && git clone https://github.com/Azure/azure-sdk-for-python.git
    && cp -r azure-sdk-for-python/azure /usr/local/lib/python2.7/dist-packages/azure

# Copies the base config into the conf.d directory
COPY confd.toml /etc/confd/confd.toml

# Install whatever else we end up needing


