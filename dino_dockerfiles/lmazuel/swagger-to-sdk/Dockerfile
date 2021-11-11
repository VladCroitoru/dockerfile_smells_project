FROM ubuntu:18.04

USER root

LABEL maintainer="lmazuel"

# Basic Ubuntu packages + Ruby (libunwind for .NET)
RUN apt-get update && apt-get install -y curl git software-properties-common locales libunwind8 ruby bundler libpng-dev zlibc zlib1g zlib1g-dev python3-pip

# NodeJS
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get update && apt-get install -y nodejs

# Go
ENV GOLANGVER=1.11
RUN curl -sLO https://dl.google.com/go/go${GOLANGVER}.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go${GOLANGVER}.linux-amd64.tar.gz
RUN ln -s /usr/local/go /root/go
ENV PATH="/root/go/bin:${PATH}"

# Go dep
ENV DEP_RELEASE_TAG=v0.5.0
RUN curl -sSL https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

# Autorest
WORKDIR /opt

# pre-load dotnet framework runtime to slim down runtime effort
RUN npm install dotnet-2.0.0

# Autorest
RUN npm install autorest@latest
RUN ln -s /opt/node_modules/.bin/autorest /usr/local/bin

# Set the locale to UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY setup.py /tmp
COPY swaggertosdk /tmp/swaggertosdk/
WORKDIR /tmp
RUN python3 -m pip install .[rest]

# Make "python" to default on Python 3. Probably breaking Ubuntu apt
# based on Python 2, but we don't care in a container
RUN ln -s /usr/bin/python3 /usr/local/bin/python

WORKDIR /git-restapi
ENTRYPOINT ["python3.6", "-m", "swaggertosdk"]
