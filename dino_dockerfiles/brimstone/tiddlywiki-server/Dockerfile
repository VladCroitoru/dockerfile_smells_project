FROM golang:alpine AS builder

ARG BUILD_DATE
ARG VCS_REF

RUN apk -U add gcc make git musl-dev

COPY . /go/src/github.com/brimstone/tiddlywiki-server/

RUN go build -o /app -ldflags "-linkmode external -extldflags \"-static\" -s -w -X main.GitCommit=${VCS_REF} -X main.BuildDate=${BUILD_DATE}" github.com/brimstone/tiddlywiki-server

FROM scratch

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/brimstone/tiddlywiki-server" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

ENV AUTH_USER= \
    AUTH_PASS=

EXPOSE 5000

COPY --from=builder /app /

ENTRYPOINT ["/app"]
