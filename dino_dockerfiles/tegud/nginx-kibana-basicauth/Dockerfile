FROM nginx:1.12.0-alpine

COPY nginx.conf /nginx.conf.tmpl
COPY run.sh /

RUN apk add --no-cache --update \
      apache2-utils \
      && chmod a+x  /run.sh

ENTRYPOINT ["/run.sh"]
