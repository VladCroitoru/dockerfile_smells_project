FROM alpine

RUN apk update && apk add git build-base
WORKDIR /tmp
RUN git clone https://github.com/google/jsonnet.git
RUN cd jsonnet && make jsonnet
RUN cp jsonnet/jsonnet /usr/local/bin
VOLUME /src
WORKDIR /src
