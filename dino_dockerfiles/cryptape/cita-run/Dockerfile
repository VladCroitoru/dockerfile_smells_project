FROM ubuntu:16.04

WORKDIR /root/cita
COPY solc /usr/bin/
COPY libgmssl.so.1.0.0 /usr/local/lib/

RUN apt-get update \
    && apt-get install -y rabbitmq-server \
                          python-pip \
                          capnproto \
                          libsnappy-dev \
                          libgoogle-perftools-dev \
                          libssl-dev \
                          libsodium* \
                          curl \
                          libcurl3 \
                          sysstat \
    && chmod +x /usr/bin/solc \
    && ln -srf /usr/local/lib/libgmssl.so.1.0.0 /usr/local/lib/libgmssl.so \
    && ldconfig \
    && pip install -U pip ethereum==2.2.0 pysodium toml \
                          jsonrpcclient[requests]==2.4.2 \
                          secp256k1==0.13.2 \
                          py_solc==1.2.2 \
                          simplejson==3.11.1 \
                          protobuf==3.4.0 \
                          pathlib==1.0.1 \
                          ecdsa \
                          pysha3>=1.0.2 \
    && rm -rf /var/lib/apt/lists \
    && rm -rf ~/.cache/pip \
    && apt-get autoremove \
    && apt-get clean \
    && apt-get autoclean
