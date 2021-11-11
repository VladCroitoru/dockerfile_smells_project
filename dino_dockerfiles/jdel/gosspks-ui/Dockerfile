FROM nginx:stable-alpine

ARG CONFD_VERSION=0.16.0
ARG GOSSPKS_UI_VERSION=${GOSSPKS_UI_VERSION:-master}
ARG GOSSPKS_UI_COMMIT=

LABEL maintainer=julien@del-piccolo.com

COPY ./confd/config/* /etc/confd/conf.d/
COPY ./confd/templates/* /etc/confd/templates/
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

COPY ./gosspks-ui/ /tmp/gosspks-ui/

RUN apk add --update --virtual .builddeps nodejs npm curl \
 && curl -L https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 -o /usr/local/bin/confd \
 && chmod +x /usr/local/bin/confd \
 && cd /tmp/gosspks-ui/ \
 && npm install --no-optional \
 && npm run build:dist \
 && mv -v build/index.html /etc/confd/templates/index.html.tmpl \
 && mv -v build/* /usr/share/nginx/html/ \
 && npm cache clean --force \
 && apk del .builddeps \
 && rm -rfv /var/cache/apk/* /tmp/* /root/.npm/

VOLUME /data/nginx/cache

WORKDIR /usr/share/nginx/html/

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
