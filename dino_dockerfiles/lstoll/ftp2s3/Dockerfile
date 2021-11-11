FROM golang:1.5.1

VOLUME ["/data/ftp2s3/cache"]
ENV FTP2S3_CACHE_DIR /data/ftp2s3/cache

ADD . /go/src/github.com/lstoll/ftp2s3

RUN cd /go/src/github.com/lstoll/ftp2s3 && go get .

CMD ["ftp2s3"]
