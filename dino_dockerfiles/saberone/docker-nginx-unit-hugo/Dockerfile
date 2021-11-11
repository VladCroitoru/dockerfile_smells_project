FROM handcraftedbits/nginx-unit-webhook:latest
MAINTAINER saberone <saberone@gmail.com> 

ARG HUGO_VERSION=v0.19

COPY data /

RUN apk update && \
  apk add git go libc-dev make && \

  mkdir -p /opt/hugo && \
  mkdir -p /opt/gopath/src/github.com/spf13 && \
  cd /opt/gopath/src/github.com/spf13 && \
  git clone https://github.com/spf13/hugo && \
  cd hugo && \
  git checkout tags/${HUGO_VERSION} && \
  export GOPATH=/opt/gopath && \
  export PATH=$PATH:$GOPATH/bin && \

  make hugo && \
  mv hugo /opt/hugo/hugo && \
  cd /opt && \
  rm -rf gopath && \

  apk del go libc-dev make

CMD [ "/bin/bash", "/opt/container/script/run-hugo.sh" ]
