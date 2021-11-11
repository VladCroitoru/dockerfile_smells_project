FROM certbot/certbot

RUN apk --update --no-cache --virtual pax add \
  paxctl \
  && paxctl -cm `which python` \
  && apk del pax
