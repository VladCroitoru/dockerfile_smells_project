FROM ubuntu:trusty

ADD etc/apt/sources.list /etc/apt/sources.list

RUN apt-get update --fix-missing && \
    apt-get install -y wget curl build-essential patch git-core openssl libssl-dev unzip ca-certificates python python-dev python-pip && \
    apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*


