ARG VERSION=1.0.0

FROM golang:1-buster AS builder
RUN apt update && apt install -y git bash wget gcc make

ARG VERSION

RUN wget -O - "https://api.github.com/repos/muety/wakapi/releases/latest" \
    | grep "tarball_url" | cut -d\" -f4 \
    | wget -O /tmp/wakapi.tar.gz -i -

WORKDIR /src/wakapi

#RUN wget -O wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
#    && chmod +x wait-for-it.sh

RUN pwd && ls -al
RUN tar -zxvf /tmp/wakapi.tar.gz --strip-components=1 -C . \
    && go mod download && go get github.com/markbates/pkger/cmd/pkger \
    && go generate && CGO_ENABLED=1 go build -o wakapi -trimpath -ldflags "-s -w -buildid="

RUN sed -i 's/listen_ipv6: ::1/listen_ipv6: /g' /src/wakapi/config.default.yml

FROM gcr.io/distroless/base-debian10
WORKDIR /app

ENV ENVIRONMENT prod
ENV WAKAPI_DB_TYPE sqlite3
ENV WAKAPI_DB_USER ''
ENV WAKAPI_DB_PASSWORD ''
ENV WAKAPI_DB_HOST ''
ENV WAKAPI_DB_NAME=/data/wakapi.db
ENV WAKAPI_PASSWORD_SALT ''
ENV WAKAPI_LISTEN_IPV4 '0.0.0.0'
ENV WAKAPI_INSECURE_COOKIES 'true'
ENV WAKAPI_ALLOW_SIGNUP 'true'

COPY --from=builder /src/wakapi/wakapi /app/
COPY --from=builder /src/wakapi/config.default.yml /app/config.yml
COPY --from=builder /src/wakapi/version.txt /
COPY --from=builder /src/wakapi/static /static
COPY --from=builder /src/wakapi/data /data
COPY --from=builder /src/wakapi/migrations /migrations
COPY --from=builder /src/wakapi/views /views
#COPY --from=builder /src/wakapi/wait-for-it.sh /app/

VOLUME /data

CMD ["/app/wakapi"]
