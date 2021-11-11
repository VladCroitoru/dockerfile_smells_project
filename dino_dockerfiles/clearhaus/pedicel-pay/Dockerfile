FROM ruby:2.3.6-alpine

LABEL maintainer="Clearhaus"

WORKDIR /opt/pedicel-pay
COPY . /opt/pedicel-pay
RUN apk update && \
    apk add make libc-dev gcc && \
    bundle install --without development

ENTRYPOINT ["/opt/pedicel-pay/exe/pedicel-pay"]
