FROM alpine:3.2  
MAINTAINER Steve Nolen <technolengy@gmail.com>

RUN apk --update add --virtual build-deps make nodejs \
  && npm install -g jade recess uglify-js

ADD . /dashboard

WORKDIR /dashboard
RUN make CAMPAIGN=snack OUT=/ohmage-frontends/dashboard

VOLUME /ohmage-frontends/dashboard
