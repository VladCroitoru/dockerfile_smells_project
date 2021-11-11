FROM python:3-alpine

LABEL maintainer="teake.nutma@gmail.com"
LABEL version="1.1"
LABEL description="Image for building Sphinx documentation"

RUN apk add --update \
    make \
  && pip --no-cache-dir install \
    sphinx \
    sphinx_rtd_theme \
  && rm -rf /var/cache/apk/*

CMD [ "/bin/sh" ]
