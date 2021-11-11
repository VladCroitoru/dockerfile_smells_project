FROM alpine:3.8

ARG BUILD_PKGS="build-base libffi-dev linux-headers openssl-dev python3-dev"
ARG MAIN_PKGS="git openssh-client python3"
ARG PY_PKGS="ansible ansible-modules-hashivault awscli boto dopy gixy hvac molecule pyapi-gitlab pycrypto testinfra yamllint"

RUN apk add --no-cache --virtual build_pkgs $BUILD_PKGS && \
  apk add --no-cache --virtual main_pkgs $MAIN_PKGS && \
  pip3 install --upgrade --no-cache-dir pip && \
  pip3 install --no-cache-dir $PY_PKGS && \
  rm -rf /var/cache/apk/* && \
  apk del build_pkgs && \
  rm -rf /root/.cache
