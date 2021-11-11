FROM alpine:3.7

RUN apk --no-cache add git py-pip python openssh-client openssl
RUN apk --no-cache add --virtual build-dependencies build-base python-dev musl-dev libffi-dev openssl-dev make \
  && pip install ansible==2.7.0 \
  && apk del build-dependencies
CMD ansible
LABEL maintainer="info@learnship.com"
