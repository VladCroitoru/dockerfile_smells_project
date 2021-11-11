FROM python:3-alpine

MAINTAINER Artur Maciag <maciag.artur@gmail.com>

ARG CROSSBAR_VERSION
ARG BUILD_DATE

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Crossbar.io Starter Template for OpenShift" \
      org.label-schema.description="Quickstart template for application development with Crossbar.io on OpenShift" \
      org.label-schema.url="https://github.com/p1c2u/openshift-crossbar" \
      org.label-schema.vcs-url="https://github.com/p1c2u/openshift-crossbar" \
      org.label-schema.vendor="Artur Maciag" \
      org.label-schema.version=$CROSSBAR_VERSION \
      org.label-schema.schema-version="1.0"

ENV HOME /node
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1

RUN apk --update upgrade \
    && apk add libffi \
    && apk add --virtual .build-deps \
               build-base \
               libffi-dev \
               openssl-dev \
               linux-headers \
    && pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir crossbar>=${CROSSBAR_VERSION} \
    && apk del .build-deps

RUN addgroup -S -g 242 crossbar \
    && adduser -S -u 242 -D -h /node -G crossbar -g "Crossbar.io Service" crossbar

COPY ./node/ /node/
RUN chown -R crossbar:crossbar /node

WORKDIR /node

USER crossbar
EXPOSE 8080 8000

ENTRYPOINT ["crossbar"]
CMD ["start", "--cbdir", "/node/.crossbar"]
