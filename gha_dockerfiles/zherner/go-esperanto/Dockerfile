FROM golang:1.15 AS base

ENV GOFLAGS -mod=vendor

# Please see the readme at github.com/kevineaton/go-esperanto

ADD . /go/src/github.com/kevineaton/go-esperanto
ADD ./phrasebook.txt /go/src/github.com/kevineaton/go-esperanto
ADD ./phrasebook.json /go/src/github.com/kevineaton/go-esperanto
WORKDIR /go/src/github.com/kevineaton/go-esperanto

RUN go build -mod=vendor .

FROM busybox:glibc
WORKDIR /go/src/github.com/kevineaton/go-esperanto
COPY --from=base /go/src/github.com/kevineaton/go-esperanto/go-esperanto .
COPY --from=base /go/src/github.com/kevineaton/go-esperanto/phrasebook.json .
COPY --from=base /go/src/github.com/kevineaton/go-esperanto/phrasebook.txt .

CMD ["./go-esperanto"]