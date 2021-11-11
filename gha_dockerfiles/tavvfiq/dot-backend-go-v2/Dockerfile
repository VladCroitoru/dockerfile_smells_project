FROM golang:1.16-stretch AS builder
WORKDIR /app
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . .
RUN GOOS="linux" GOARCH=amd64 CGO_ENABLED=0 go build -o article-api

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/.local.env .
COPY --from=builder /app/article-api .
ARG PORT
EXPOSE  ${PORT}
CMD ["/app/article-api"]
