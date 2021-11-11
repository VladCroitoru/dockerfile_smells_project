FROM golang:1.10.0-stretch as BUILD

ENV DEBIAN_FRONTED noninteractive

RUN apt update

RUN go get -v github.com/rubenv/sql-migrate/...

FROM gcr.io/distroless/base

COPY --from=BUILD /go/bin/sql-migrate /bin/sql-migrate

COPY --from=BUILD /bin/sh /bin/sh

COPY --from=BUILD /bin/ls /bin/ls

ENV CONFIG ""

ENV PATH="/bin"

ADD run.sh /bin/run.sh

ENTRYPOINT ["/bin/run.sh"]

CMD ["status"]