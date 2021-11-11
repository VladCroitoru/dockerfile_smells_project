FROM minio/minio:latest

RUN apk add --update bash openssl

ADD run-minio /bin/run-minio

ENTRYPOINT ["/bin/run-minio"]
