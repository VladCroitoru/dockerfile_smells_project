# docker build -t mpapec/convos .
FROM alpine:3.4
MAINTAINER mpapec@irc://irc.freenode.net/#convos

RUN apk update && \
  apk add perl perl-io-socket-ssl perl-dev g++ make openssl openssl-dev wget curl && \
  curl -L https://goo.gl/kDpvKZ | tar xvz && \
  ln -s /convos-stable /convos && \
  cd /convos && \
  perl script/convos install && \
  apk del perl-dev g++ make openssl openssl-dev wget curl && \
  rm -rf /root/.cpanm/* /usr/local/share/man/*

# USER daemon
WORKDIR /convos
ENV CONVOS_HOME /data
VOLUME ["/data"]

EXPOSE 3000
CMD ["perl", "script/convos", "daemon"]
# docker run -it --rm -p 3000:3000 -v /tmp/data:/data mpapec/convos
