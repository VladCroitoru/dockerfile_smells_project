FROM alpine:3.7 AS resource

RUN apk --no-cache add \
  bash \
  curl \
  git \
  git-daemon \
  gnupg \
  gzip \
  jq \
  openssh \
  perl \
  tar \
  openssl \
  libstdc++ \
  python3

RUN pip3 install --upgrade awscli awslogs

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
