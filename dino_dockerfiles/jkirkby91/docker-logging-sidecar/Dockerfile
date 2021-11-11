FROM jkirkby91/ubuntusrvbase:latest
MAINTAINER James Kirkby <james.kirkby@sonyatv.com>

ARG APP_NAME=APP_NAME
ARG TARGET_SERVICE=TARGET_SERVICE

ENV APP_NAME=${APP_NAME}
ENV TARGET_SERVICE=${TARGET_SERVICE}

RUN printenv

VOLUME ["/data/logs"]
