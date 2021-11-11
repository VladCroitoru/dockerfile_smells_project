FROM democracyos/democracyos:2.11.13

MAINTAINER Muni <matias@democraciaenred.org>

COPY ./dos-overrides/lib/db-api/user.js /usr/src/lib/db-api/user.js

ENV LOCALE=es \
  ENFORCE_LOCALE=true \
  AVAILABLE_LOCALES=es,en \
  MULTI_FORUM=true \
  RESTRICT_FORUM_CREATION=true \
  LOGO=/ext/lib/boot/logo.svg \
  LOGO_MOBILE=/ext/lib/boot/logo.svg \
  ORGANIZATION_EMAIL=no-reply@rosario.gob.ar \
  ORGANIZATION_NAME='Municipalidad de Rosario' \
  ORGANIZATION_URL=http://rosario.gob.ar \
  SOCIALSHARE_DOMAIN=participa.rosario.gob.ar \
  SOCIALSHARE_IMAGE=https://cldup.com/quswAMk9Ns.png \
  SOCIALSHARE_SITE_NAME='Rosario Participa' \
  SOCIALSHARE_TWITTER_USERNAME='@RParticipa' \
  SOCIALSHARE_SITE_DESCRIPTION='Plataforma de participación de la ciudad de Rosario' \
  BLACK_LIST_EMAILS=pokemail.net,grr.la,yopmail.com,sharklasers.com
