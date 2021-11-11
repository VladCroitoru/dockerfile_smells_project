FROM ubuntu:18.04

# ENV TZ=Europe/Amsterdam
ENV TZ=Etc/UTC
ENV LANG=C.UTF-8

# Here we install mongo-tools. It's actually version 3.6, so older than
# the databse, but it's compatible by adding --forceTableScan

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    mongo-tools \
    awscli \
    wget \
    ca-certificates \
    curl \
    gnupg2 \
    lsb-release \
    redis-tools \
    vim \
    webfs \
    netcat \
    bzip2 \
    screen \
    unzip

## New dig (w.o. perl)
RUN apt-get install -y \
    knot-dnsutils \
    && ln -s /usr/bin/kdig /usr/bin/dig

## Postgres client
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' \
    && apt-get update && apt-get install -y postgresql-client-11

# Minio S3 Client
RUN wget --quiet -O /usr/local/sbin/mc https://dl.min.io/client/mc/release/linux-amd64/mc && chmod +x /usr/local/sbin/mc

# Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl \
    && mv kubectl /usr/local/bin \
    && chmod +x /usr/local/bin/kubectl

# Rclone
RUN curl https://rclone.org/install.sh | sudo bash


# A simple webserver
RUN printf "#!/bin/sh\nwebfsd -F -p 8000 -r /var/local/\n" >> /usr/local/bin/webserver && chmod +x /usr/local/bin/webserver

## Run
CMD ["sh", "-c", "echo 'starting tools' && while true; echo -n '.'; do sleep 7; done;"]