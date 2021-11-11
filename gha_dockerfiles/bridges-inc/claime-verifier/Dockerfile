FROM golang:1.16-alpine as builder

LABEL maintainer="Yushi Masui <yushi.masui@bridges.inc>"

WORKDIR /app
COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY . .
COPY lib/functions/joinguild/main.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:latest  

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /app/main .

CMD ["./main"] 

