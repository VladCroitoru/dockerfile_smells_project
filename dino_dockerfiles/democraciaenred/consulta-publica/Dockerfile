FROM democracyos/democracyos:2.11.15

MAINTAINER Democracia en Red <it@democracyos.io>

COPY ./dos-override/models/comment.js /usr/src/lib/models/comment.js
COPY ./dos-override/api-v2/db-api/comments/index.js /usr/src/lib/api-v2/db-api/comments/index.js
COPY ./dos-override/api-v2/db-api/comments/scopes.js /usr/src/lib/api-v2/db-api/comments/scopes.js
COPY ./dos-override/api-v2/db-api/users/scopes.js /usr/src/lib/api-v2/db-api/users/scopes.js

ENV LOCALE=es \
  AVAILABLE_LOCALES=es,en \
  ENFORCE_LOCALE=true \
  MODERATOR_ENABLED=true \
  MULTI_FORUM=true \
  RESTRICT_FORUM_CREATION=true \
  FAVICON=/ext/lib/boot/favicon.ico \
  LOGO=/ext/lib/site/footer/logo-footer.svg \
  LOGO_MOBILE=/ext/lib/site/footer/logo-footer.svg \
  NOTIFICATIONS_MAILER_EMAIL=gobiernoabierto@modernizacion.gob.ar \
  NOTIFICATIONS_MAILER_NAME='Consulta Pública Argentina' \
  ORGANIZATION_EMAIL=gobiernoabierto@modernizacion.gob.ar \
  ORGANIZATION_NAME='Consulta Pública Argentina' \
  SOCIALSHARE_SITE_NAME='Consulta Pública Argentina' \
  SOCIALSHARE_SITE_DESCRIPTION='Plataforma de participación ciudadana de la República Argentina.' \
  SOCIALSHARE_IMAGE=https://cldup.com/Y7mWiU4D1Q.png \
  SOCIALSHARE_DOMAIN=consultapublica.argentina.gob.ar \
  SOCIALSHARE_TWITTER_USERNAME=@ModernizacionAR \
  TWEET_TEXT='Estoy tratando de mejorar esta propuesta “{topic.mediaTitle}” ¡Participá vos también! #GobiernoAbierto'
