FROM alpine:3.4
MAINTAINER teaegg <teaegg.love@gmail.com>

ENV RUNTIME_PACKAGES python py-pip libxslt libxml2 git curl libpq
ENV BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev python-dev openssl-dev postgresql-dev

RUN apk add --no-cache ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip install git+https://github.com/scrapy/scrapy.git \
              git+https://github.com/scrapy/scrapyd.git \
              git+https://github.com/scrapy/scrapyd-client.git \
              git+https://github.com/scrapinghub/scrapy-splash.git \
              simplejson \
              psycopg2 && \
  curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion >> /root/.bashrc && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache

ADD ./scrapyd.conf /etc/scrapyd/

EXPOSE 6800

CMD ["scrapyd"]
