FROM smartentry/alpine:3.5-0.3.15

MAINTAINER Yifan Gao <docker@yfgao.com>

ADD .docker $ASSETS_DIR

RUN smartentry.sh build

CMD ["supervisord"]
