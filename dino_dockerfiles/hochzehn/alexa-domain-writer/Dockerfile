FROM docker:1.11.2

RUN apk add --no-cache \
  bash \
  curl \
 parallel

ADD ./app /opt/app

WORKDIR /opt/app

ENTRYPOINT ["./entrypoint.sh"]
CMD [""]
