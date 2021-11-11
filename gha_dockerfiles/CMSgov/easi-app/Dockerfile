FROM golang:1.16.6 AS base

WORKDIR /easi/

FROM base AS modules

COPY go.mod ./
COPY go.sum ./
RUN go mod download

FROM modules AS build

COPY cmd ./cmd
COPY pkg ./pkg

RUN CGO_ENABLED=0 GOOS=linux go build -a -o bin/easi ./cmd/easi

COPY config/tls/rds-ca-2019-root.pem /usr/local/share/ca-certificates/rds-ca-2019-root.crt
COPY config/tls/hhs-fpki-intermediate-ca.pem /usr/local/share/ca-certificates/hhs-fpki-intermediate-ca.crt
RUN update-ca-certificates

FROM modules AS dev

RUN go get golang.org/x/tools/gopls@latest
RUN go get github.com/cosmtrek/air@895210e492af4a2dc1c5286e7c4a45cc4d8452a7
CMD ["./bin/easi"]

FROM gcr.io/distroless/base:latest

WORKDIR /easi/
COPY --from=build /easi/bin/easi .
COPY --from=build /easi/pkg/email/templates ./templates
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs

ARG ARG_APPLICATION_VERSION
ARG ARG_APPLICATION_DATETIME
ARG ARG_APPLICATION_TS
ENV APPLICATION_VERSION=${ARG_APPLICATION_VERSION}
ENV APPLICATION_DATETIME=${ARG_APPLICATION_DATETIME}
ENV APPLICATION_TS=${ARG_APPLICATION_TS}
ENV EMAIL_TEMPLATE_DIR=/easi/templates

USER 1000

ENTRYPOINT ["/easi/easi"]

CMD ["serve"]
