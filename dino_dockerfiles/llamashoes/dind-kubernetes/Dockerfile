FROM ubuntu:14.04
MAINTAINER rgifford@gmail.com

# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    lxc \
    iptables
    
# Install Docker from Docker Inc. repositories.
RUN apt-get install curl supervisor -y
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
RUN sh -c "echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
RUN apt-get update;apt-get install -y lxc-docker
RUN mkdir /repos

# Supervisor Setup
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Install kubernetes and golang
WORKDIR /repos
RUN git clone https://github.com/GoogleCloudPlatform/kubernetes.git
RUN wget https://storage.googleapis.com/golang/go1.3.3.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.3.3.linux-amd64.tar.gz
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/go/bin

# Install etcd
WORKDIR /repos/kubernetes
RUN hack/travis/install-etcd.sh
RUN cp third_party/etcd/* /usr/bin/

# Open apisever to all interfaces
RUN sed -i '/API_HOST=${API_HOST:-127.0.0.1}/ c\API_HOST=${API_HOST:-0.0.0.0}' /repos/kubernetes/hack/local-up-cluster.sh
RUN sed -i '/API_PORT=${API_PORT:-8080}/ c\API_PORT=${API_PORT:-8888}' /repos/kubernetes/hack/local-up-cluster.sh
WORKDIR /

ADD start.sh /start.sh
RUN chmod +x /start.sh

# Define additional metadata for our image.
VOLUME /var/lib/docker

# Start supervisord
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
