FROM phusion/baseimage:latest
MAINTAINER Arne Jørgensen <arne@reload.dk>

RUN set -x && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -q golang-go git php-cli php-curl ruby python-pip && \
    GOPATH=/usr/local go get -u github.com/xenolf/lego && \
    curl -sS https://platform.sh/cli/installer | php && \
    curl -sS -o /opt/yamledit.rb https://raw.githubusercontent.com/dbrandenburg/yamledit/e277715d71ed5bac17e97267577dd612fcc7ee2c/yamledit.rb && \
    pip install shyaml && \
    DEBIAN_FRONTEND=noninteractive apt-get purge -y -q golang-go python-pip && \
    apt-get clean -y -q && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH=/root/.platformsh/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

COPY etc/ /etc/
COPY usr/ /usr/
VOLUME [ "/data" ]
