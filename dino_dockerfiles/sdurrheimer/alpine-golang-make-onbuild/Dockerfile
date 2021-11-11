FROM        sdurrheimer/alpine-glibc
MAINTAINER  The Prometheus Authors <prometheus-developers@googlegroups.com>

RUN addgroup -S golang && adduser -S -G golang golang

COPY go-build /bin/go-build
COPY go-run /bin/go-run
COPY helper.mak /bin/helper.mak

RUN     mkdir -p /app
WORKDIR /app

ONBUILD COPY    . /app
ONBUILD RUN     /bin/go-build
ONBUILD WORKDIR /bin
ONBUILD USER    golang

ENTRYPOINT  ["/bin/go-run"]
