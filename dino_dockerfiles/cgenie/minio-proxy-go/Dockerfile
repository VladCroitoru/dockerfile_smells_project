FROM golang:1.9.7-alpine

RUN apk add --no-cache curl git

COPY ./ /go

WORKDIR /go
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
RUN cd /go/src/minio-proxy-go && dep init && dep ensure
RUN go install minio-proxy-go

ENTRYPOINT ["/bin/sh", "-c"]
#CMD ["/code/docker/minio-proxy-startup.sh"]
CMD ["minio-proxy-go"]
