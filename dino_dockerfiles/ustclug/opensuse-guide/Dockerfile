FROM smartentry/alpine:3.5-0.3.14

ADD .docker $ASSETS_DIR

RUN smartentry.sh build

ADD . /var/www
