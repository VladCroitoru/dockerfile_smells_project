FROM registry.redhat.io/rhel8/go-toolset:1.15 AS builder
WORKDIR $GOPATH/src/mypackage/myapp/
COPY . .
ENV GO111MODULE=on
USER root
RUN go get -d -v
RUN CGO_ENABLED=0 go build -o /go/bin/quickstarts

# Build the migration binary.
RUN CGO_ENABLED=0 go build -o /go/bin/quickstarts-migrate cmd/migrate/migrate.go

 
FROM registry.redhat.io/ubi8-minimal:latest

COPY --from=builder /go/bin/quickstarts /usr/bin
COPY --from=builder /go/bin/quickstarts-migrate /usr/bin
COPY --from=builder /src/mypackage/myapp/spec/openapi.json /var/tmp

USER 1001


CMD ["quickstarts"]
EXPOSE 8000