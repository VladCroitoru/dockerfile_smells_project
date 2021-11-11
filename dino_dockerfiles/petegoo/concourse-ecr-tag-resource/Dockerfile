FROM python:3.6.4-alpine3.7 as builder

RUN mkdir /app
COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3 setup.py sdist


FROM alpine:edge
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

COPY --from=builder /app/dist/concourse-ecr-tag-resource-*.tar.gz .
RUN pip3 install concourse-ecr-tag-resource-*.tar.gz
RUN mkdir -p /opt/resource
RUN for script in check in out; do ln -s $(which $script) /opt/resource/; done
