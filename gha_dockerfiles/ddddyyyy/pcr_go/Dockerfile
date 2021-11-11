FROM golang:latest
WORKDIR /go/src/app
COPY ./ /go/src/app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o pcr .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
RUN apk --no-cache add curl
WORKDIR /root/
COPY --from=0 go/src/app/pcr .
CMD ["./pcr"]
LABEL version=demo-3