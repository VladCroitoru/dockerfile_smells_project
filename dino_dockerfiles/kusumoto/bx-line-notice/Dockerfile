FROM golang:1.8-onbuild
WORKDIR /go/src/github.com/kusumoto/bx-line-notice
ADD ./ .
RUN go get github.com/spf13/viper
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/kusumoto/bx-line-notice .
CMD ["./main"]  