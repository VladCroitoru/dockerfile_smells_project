FROM alpine:3.7

RUN apk add --no-cache \
      shadow \
      su-exec \
      docker \
      python

RUN apk add --no-cache --virtual .build-dependencies \
      py-pip \
 && pip install awscli \
 && apk --purge del \
      .build-dependencies

COPY usr /usr

ENTRYPOINT ["entrypoint.sh"]
