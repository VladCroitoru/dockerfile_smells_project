FROM ubuntu

MAINTAINER Robin Kearney <robin@kearney.co.uk>

ENV helmVersion "3.5.3"
ENV jamalVersion "1.0.0"

RUN apt-get update
RUN apt-get install -y \
        curl \
        dnsutils \
        htop \
        jq \
        lsof \
        netcat \
        nmap \
        python-pip \
        ssh \
        tcpflow \
        vim \
        postgresql-client \
        && \
        pip install awscli

RUN curl -LOs https://get.helm.sh/helm-v${helmVersion}-linux-amd64.tar.gz &&\
    tar xzvf helm-v${helmVersion}-linux-amd64.tar.gz &&\
    cp linux-amd64/helm /usr/local/bin &&\
    chmod +x /usr/local/bin/helm &&\
    rm -rf linux-amd64 *.tar.gz

RUN curl -LOs https://github.com/quantumew/jamal/releases/download/v${jamalVersion}/jamal-v${jamalVersion}.tar.gz &&\
    tar xzvf jamal-v${jamalVersion}.tar.gz jamal-v${jamalVersion}/linux/386/jamal --strip-components=3 &&\
    mv jamal /usr/local/bin &&\
    chmod +x /usr/local/bin/jamal &&\
    rm -rf jamal-v${jamalVersion}.tar.gz

RUN rm -rf /var/lib/apt/lists/*
