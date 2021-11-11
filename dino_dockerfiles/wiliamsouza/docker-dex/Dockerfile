FROM golang:1.8

MAINTAINER Anthony Smith <anthony@sticksnleaves.com>

ENV DEX_HOME /go/src/github.com/coreos/dex
ENV DEX_VERSION 2.3.0
ENV PATH $DEX_HOME/bin:$PATH

RUN apt-get update -y && \
    apt-get install sqlite3 -y && \
    apt-get clean -y

RUN mkdir -p $DEX_HOME

RUN curl -L https://github.com/coreos/dex/archive/v$DEX_VERSION.tar.gz | tar zx && \
    cp -R dex-$DEX_VERSION/* $DEX_HOME && \
    rm -rf dex-$DEX_VERSION

RUN cd $DEX_HOME && \
    make

WORKDIR $DEX_HOME

EXPOSE 5554-5557

ENTRYPOINT ["dex"]

VOLUME ["/etc/dex"]

CMD ["version"]
