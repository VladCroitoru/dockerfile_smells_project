FROM ubuntu AS down

ENV OF_VER=5-0
WORKDIR /data/
RUN apt-get update \
 && apt-get install -y wget \
 && wget -qO - http://dl.openfoam.org/source/${OF_VER} | tar xz --strip-components=1 --wildcards --no-anchored '*/tutorials/*'

FROM golang:1.9 AS build

WORKDIR /go/src/github.com/qnib/example
COPY main.go .
RUN go build -ldflags "-linkmode external -extldflags -static" -a main.go

FROM scratch
COPY --from=build /go/src/github.com/qnib/example/main /main
COPY --from=down /data/tutorials /tutorials
CMD ["/main"]
