FROM ubuntu:16.04

RUN apt-get update \
    && apt-get -qq --no-install-recommends install \
        libcurl3 \
    && rm -r /var/lib/apt/lists/*

RUN set -x \
    && buildDeps=' \
        automake \
        ca-certificates \
        cuda-core-8-0 \
        cuda-cudart-dev-8-0 \
        libcurl4-openssl-dev \
        libssl-dev \
        wget \
    ' \
    && apt-get -qq update \
    && apt-get -qq --no-install-recommends install wget \
    && wget -q http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.44-1_amd64.deb \
    && dpkg -i cuda-repo-ubuntu1604_8.0.44-1_amd64.deb \
    && rm cuda-repo-ubuntu1604_8.0.44-1_amd64.deb \
    && apt-get -qq update \
    && apt-get -qq --no-install-recommends install cuda-cudart-8-0 \
    && apt-get -qq --no-install-recommends install $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /usr/local/src/ccminer \
    && cd /usr/local/src/ccminer \
    && wget -qO - https://github.com/tpruvot/ccminer/archive/v2.2-tpruvot.tar.gz | tar -xz --strip-components=1 \
    && ./autogen.sh \
    && ./configure --with-cuda=/usr/local/cuda-8.0 \
    && make -j"$(nproc)" \
    && make install \
    && cd .. \
    && rm -r ccminer \
    && apt-get -qq --auto-remove purge $buildDeps

ENTRYPOINT ["ccminer"]