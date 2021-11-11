FROM golang:1.16.5-alpine3.14 as builder

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN go get -u github.com/gin-gonic/gin
RUN go build -o main .

FROM alpine:latest
RUN mkdir /app
WORKDIR /app
COPY --from=builder /app/main /app/
CMD ["/app/main"]
