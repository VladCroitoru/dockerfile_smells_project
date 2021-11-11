FROM alpine:3.7

RUN apk add --no-cache curl tzdata

ADD entrypoint.sh VERSION /

CMD ["/bin/sh", "/entrypoint.sh"]