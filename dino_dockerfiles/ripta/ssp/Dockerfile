FROM golang:1.14 AS builder

ENV CGO_ENABLED=0
ENV GO111MODULE=on

ARG BUILD_DATE
ARG VERSION

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -v -ldflags "-s -w -X main.BuildVersion=$VERSION -X main.BuildDate=$BUILD_DATE -X main.BuildEnvironment=prod" -o bin/ssp ./cmd/ssp


FROM alpine
COPY --from=builder /app/bin/ssp /app/bin/ssp
COPY examples/userdir.yaml /app/config.yaml
ENTRYPOINT ["/app/bin/ssp"]
CMD ["--config=/app/config.yaml"]
