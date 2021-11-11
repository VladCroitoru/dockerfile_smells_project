FROM registry.redhat.io/ubi8/go-toolset as builder

WORKDIR /go/src/app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

USER root

RUN go build -o pt-api ./cmd/payload-tracker-api/main.go && \
    go build -o pt-consumer ./cmd/payload-tracker-consumer/main.go && \
    go build -o pt-migration internal/migration/main.go

FROM registry.redhat.io/ubi8/ubi-minimal

WORKDIR /

# Copy executable files from the builder image
COPY --from=builder /go/src/app/pt-api /pt-api
COPY --from=builder /go/src/app/pt-consumer /pt-consumer
COPY --from=builder /go/src/app/pt-migration /pt-migration

USER 1001

CMD ["/pt-api"]