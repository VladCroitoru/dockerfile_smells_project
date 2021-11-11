FROM alpine:3.3
RUN apk update \
 && apk add vim
USER nobody
ENV HOME=/tmp
ENTRYPOINT ["/usr/bin/vim"]
