# syntax=docker/dockerfile:1
FROM golang:latest AS builder

WORKDIR /install

COPY . /install
RUN rm -rf go.sum; \
    go get all
RUN go install cmd/worker/opp_edge_worker.go; \
    go install cmd/config/opp_edge_config.go; \
    go install cmd/broker/opp_edge_broker.go; \
    go install cmd/consumer/opp_edge_run.go; \
    go install cmd/stargate_client/stargate_client.go; \
    go install cmd/stargate_server/stargate_server.go

FROM pzierahn/omnetpp
WORKDIR /root

COPY --from=builder /go/bin/ /bin/
