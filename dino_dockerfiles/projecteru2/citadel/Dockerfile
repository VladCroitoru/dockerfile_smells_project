FROM python:3.6.4-alpine

MAINTAINER timfeirg <kkcocogogo@gmail.com>

RUN mkdir -p /opt/citadel
ADD . /opt/citadel
WORKDIR /opt/citadel
RUN apk add --no-cache alpine-sdk libstdc++ && \
	pip install -U -r requirements.txt && \
	apk del alpine-sdk
ENV GRPC_VERBOSITY=INFO C_FORCE_ROOT=true
