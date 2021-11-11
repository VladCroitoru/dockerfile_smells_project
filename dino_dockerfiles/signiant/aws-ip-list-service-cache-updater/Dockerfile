FROM alpine:latest

# bash
RUN apk -Uuv add coreutils bash bash-doc bash-completion curl && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

RUN mkdir -p /app

WORKDIR /app

VOLUME /json

COPY app/* ./
RUN chmod a+x *

ENTRYPOINT ["./cache-freshener.sh"]
CMD ['']
