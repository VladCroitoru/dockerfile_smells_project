FROM golang:1.8.0-alpine

RUN apk --update --no-cache add \
      git && \
    go get \
      github.com/GoogleCloudPlatform/cloudsql-proxy/cmd/cloud_sql_proxy
WORKDIR /cloudsql-proxy
COPY run.sh .

CMD sh run.sh
