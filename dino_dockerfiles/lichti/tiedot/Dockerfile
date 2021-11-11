FROM golang:1.8.3 as builder
ARG CGO_ENABLED=0
ARG GOOS=linux
WORKDIR /go/src/tiedot
COPY ./    .
RUN go get  -v -d .
RUN CGO_ENABLED=$CGO_ENABLED GOOS=$GOOS go build -a -installsuffix cgo -o /tiedot .

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /tiedot /bin/
EXPOSE 8080
VOLUME ["/data"]
CMD ["tiedot","-dir","/data","-port","8080","-mode","httpd"]
