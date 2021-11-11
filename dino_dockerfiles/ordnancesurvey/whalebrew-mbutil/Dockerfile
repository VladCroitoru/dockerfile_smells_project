FROM python:2.7-alpine

RUN apk add --no-cache git \
 && cd /usr/local \
 && git clone git://github.com/mapbox/mbutil.git \
 && apk del git

LABEL io.whalebrew.name mb-util
ENTRYPOINT ["/usr/local/mbutil/mb-util"]
