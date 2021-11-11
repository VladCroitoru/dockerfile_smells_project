FROM golang:1.8-alpine AS builder
COPY . /go/src/github.com/tonistiigi/dockerfile
RUN CGO_ENABLED=0 go build -o /dockerfile-frontend --ldflags '-extldflags "-static"' github.com/tonistiigi/dockerfile/cmd/dockerfile-frontend

FROM scratch
COPY --from=builder /dockerfile-frontend /bin/dockerfile-frontend
ENTRYPOINT ["/bin/dockerfile-frontend"]