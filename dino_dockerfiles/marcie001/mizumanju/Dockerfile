FROM golang:1.4.2-wheezy

MAINTAINER marcie001 <marcie00001@gmail.com>

RUN go get bitbucket.org/liamstask/goose/cmd/goose
RUN go get github.com/marcie001/mizumanju/cmd/mizumanju

WORKDIR /work
ADD ./entrypoint.sh /work/
ADD ./db /work/db

ENV DATABASE_URL_GOOSE=tcp:db:3306*mizumanju/root/password \
    DATABASE_URL=root:password@tcp(db:3306)/mizumanju?charset=utf8mb4&parseTime=true \
    LISTEN_IP= \
    MAIL_ADDRESS=foo@example.com \
    NAME=Mizumanju \
    LISTEN_PORT=8080 \
    DEBUG_SERVER=false \
    SMTP_HOST=127.0.0.1 \
    SMTP_PORT=25 \
    SMTP_START_TLS=false \
    SMTP_USER= \
    SMTP_PASSWORD= \
    BASE_URL=http://127.0.0.1/

ENTRYPOINT ["./entrypoint.sh"]
