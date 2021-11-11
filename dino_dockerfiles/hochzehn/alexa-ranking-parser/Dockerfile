FROM alpine:3.3

RUN apk add --no-cache \
  bash \
  wget \
  unzip \
  parallel \
  curl

ADD ./app /opt/app
ADD ./app/tmp /opt/app

WORKDIR /opt/app

ENTRYPOINT ["./entrypoint.sh"]
CMD [""]
