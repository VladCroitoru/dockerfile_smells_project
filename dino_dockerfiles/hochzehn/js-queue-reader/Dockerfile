FROM alpine:3.3

RUN apk add --no-cache \
  bash \
  curl

ADD ./app /opt/app
WORKDIR /opt/app

ENTRYPOINT ["./entrypoint.sh"]
CMD [""]
