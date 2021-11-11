FROM alpine:edge

RUN apk add --update findutils docker make git openssh-client yamllint ansible ansible-lint terraform zip openssh-client && rm -rf /var/cache/apk/*

RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing openssh-askpass

ENTRYPOINT [ "/bin/sh", "-c", "/bin/sh" ]
