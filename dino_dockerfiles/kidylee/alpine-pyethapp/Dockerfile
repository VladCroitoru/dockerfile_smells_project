# build with `docker build -t localethereum/client-python .`
FROM alpine

MAINTAINER An Li kidylee@gmail.com

WORKDIR ethereum

RUN apk add --no-cache --update python py-pip \
	&& apk add --no-cache --update --virtual .build-deps\
		alpine-sdk \
		make \
		g++ \
		musl-dev \
		autoconf \
		automake \
		libtool \
		libffi-dev \
		gmp-dev \
		python-dev \
		openssl-dev

RUN git clone https://github.com/ethereum/pyrlp /ethereum/pyrlp
WORKDIR /ethereum/pyrlp
RUN pip install --no-cache-dir -e .

RUN git clone https://github.com/ethereum/pydevp2p /ethereum/pydevp2p
WORKDIR /ethereum/pydevp2p
RUN pip install --no-cache-dir -e .

RUN git clone https://github.com/ethereum/pyethereum /ethereum/pyethereum
WORKDIR /ethereum/pyethereum
RUN pip install --no-cache-dir -e .


RUN git clone https://github.com/ethereum/pyethapp /ethereum/pyethapp
WORKDIR /ethereum/pyethapp
RUN pip install --no-cache-dir -e .


RUN apk del .build-deps \
	&& apk add --update --no-cache gmp \
	&& apk add --update --no-cache leveldb -X http://dl-cdn.alpinelinux.org/alpine/edge/testing

ENTRYPOINT /usr/bin/pyethapp

