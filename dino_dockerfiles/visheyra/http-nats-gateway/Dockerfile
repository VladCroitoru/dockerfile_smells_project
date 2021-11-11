FROM golang:1.10 as build

RUN apt install make

COPY . /go/src/github.com/visheyra/http-nats-gateway

RUN make -C /go/src/github.com/visheyra/http-nats-gateway

FROM gcr.io/distroless/base

COPY --from=build /go/bin/hng /bin/hng

ENTRYPOINT ["/bin/hng"]
