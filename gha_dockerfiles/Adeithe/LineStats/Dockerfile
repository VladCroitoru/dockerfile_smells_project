FROM golang:alpine AS builder
RUN apk --update upgrade && apk add --no-cache git && rm -rf /var/cache/apk/*
WORKDIR /app
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-w -s" -o /go/bin/linestats ./cmd/bot

FROM alpine
WORKDIR /app
COPY --from=builder /go/bin/linestats ./linestats
EXPOSE 9091
ENTRYPOINT ["./linestats"]
