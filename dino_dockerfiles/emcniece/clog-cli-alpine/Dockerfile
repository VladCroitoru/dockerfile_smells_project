FROM frolvlad/alpine-rust:latest

ENV BRANCH master

RUN apk add --no-cache git \
 && git clone -b $BRANCH https://github.com/clog-tool/clog-cli

WORKDIR clog-cli

VOLUME ["/output"]

ADD entrypoint.sh /

CMD /entrypoint.sh
