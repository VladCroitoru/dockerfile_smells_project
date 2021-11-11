FROM alpine:latest

RUN mkdir /root/.chamberlain

ADD     . /opt/chamberlain
WORKDIR /opt/chamberlain

RUN apk add --no-cache libffi-dev musl-dev openssl-dev py-pip python-dev python make git gcc
RUN make

ENTRYPOINT [ "chamberlain" ]
