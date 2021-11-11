FROM alpine
MAINTAINER Danillo Nunes <marcus@danillo.net>

RUN apk add --update \
      duplicity \
    && \

    rm -rf /var/cache/apk/*

WORKDIR "/root"

COPY ["entrypoint.sh", "."]

ENTRYPOINT ["./entrypoint.sh"]

CMD ["/bin/sh"]
