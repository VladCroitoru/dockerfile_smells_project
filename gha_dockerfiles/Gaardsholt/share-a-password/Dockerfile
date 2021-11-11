FROM golang:1.17.1-alpine AS builder
WORKDIR $GOPATH/src/app
COPY . .
RUN GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o /tmp/app

FROM alpine
RUN mkdir /app
WORKDIR /app
COPY --from=builder /tmp/app app
ADD ./static static/
ADD ./templates templates/

RUN addgroup -S appgroup && adduser -S appuser -G appgroup && chown -R appuser /app

USER appuser
CMD ["/app/app"]