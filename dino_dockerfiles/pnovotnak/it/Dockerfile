FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive
ENV PATH            "$PATH:/usr/share/bcc/tools/"
ENV LANG            en_US.UTF-8

VOLUME [ "/lib/modules" ]

# Install packages
RUN set -ex; \
  apt-get update; \
  apt-get install -qy \
    apt-transport-https \
    bc \
    bpfcc-tools \
    curl \
    dnsutils \
    git \
    htop \
    iftop \
    inetutils-ping \
    iotop \
    mtr \
    netcat \
    nethogs \
    net-tools \
    nmap \
    pv \
    strace \
    sudo \
    tcpdump \
    tmux \
    traceroute \
    vim \
    wget; \
  rm -rf /var/lib/apt/lists/* ; \
  curl -Lo /usr/local/bin/kubectl \
    https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl; \
  chmod +x /usr/local/bin/kubectl

# Install .files
COPY .files /root/.files/
RUN yes | $HOME/.files/install.sh

COPY --from=fortio/fortio:latest /usr/bin/fortio /usr/local/bin/fortio

# Final runtime env setup
WORKDIR /root
CMD tmux

