FROM ubuntu:16.04

ARG LAGOPUS_VERSION=v0.2.10

# Install Required packages
RUN apt-get update -y -q \
  && apt-get install -y -qq build-essential linux-headers-$(uname -r) \
    libexpat-dev libgmp-dev \
    libssl-dev libpcap-dev byacc flex git \
    python-dev python-pastedeploy python-paste python-twisted \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Clone lagopus source
RUN if [ -n "${http_proxy}" ]; then git config --global http.proxy $http_proxy; fi
WORKDIR /usr/local/src
RUN git clone -b ${LAGOPUS_VERSION} --recursive https://github.com/lagopus/lagopus.git

# Build and Install
WORKDIR /usr/local/src/lagopus
RUN ./configure \
  && make gcc-full-opt \
  && make install

CMD ['lagopus']
