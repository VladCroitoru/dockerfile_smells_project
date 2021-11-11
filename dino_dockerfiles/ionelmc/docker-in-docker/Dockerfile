FROM ubuntu:xenial

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update \
 && apt-get install -y --no-install-recommends software-properties-common curl ca-certificates apt-transport-https \
 && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
 && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
                    docker-ce \
                    locales \
                    strace gdb lsof locate net-tools htop iputils-ping dnsutils \
                    python3-dbg libpython3-dbg \
                    nano vim tree less \
                    socat telnet \
                    openssh-client \
                    graphviz \
 && rm -rf /var/lib/apt/lists/*
RUN locale-gen en_US.UTF-8

ENV TERM=xterm
ARG PYTHON_PIP_VERSION=9.0.3
RUN bash -o pipefail -c "curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python3 - --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION"

ARG DOCKER_COMPOSE_VERSION=1.19.0
RUN pip install --no-cache-dir docker-compose==$DOCKER_COMPOSE_VERSION
