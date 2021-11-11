FROM alpine:latest

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/teran/staticd.git" \
      org.label-schema.vcs-ref=$VCS_REF

EXPOSE 8080

RUN apk add --update --no-cache ca-certificates && \
    rm -rvf /var/cache/apk/*

ADD bin/staticd-linux-amd64 /staticd

ENTRYPOINT ["/staticd"]
