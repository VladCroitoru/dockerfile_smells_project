FROM jphastings/credence:dependencies
ADD . /go/src/github.com/jphastings/credence
WORKDIR /go/src/github.com/jphastings/credence
RUN make bootstrap

EXPOSE 80
EXPOSE 27336
EXPOSE 27334

ENTRYPOINT serverconfig/start
