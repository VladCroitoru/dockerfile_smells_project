FROM node:12 as builder

ADD . /web-grid/
RUN cd web-grid && npm install && npm run build

FROM nginx:latest
ADD ./custom-nginx/default.conf /tmp/template.conf
COPY --from=builder ./web-grid/build/ /usr/share/nginx/html
EXPOSE 80
RUN     DEBIAN_FRONTEND=noninteractive \
        && apt-get update \
        && apt-get -y install gettext-base \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*
CMD envsubst < /tmp/template.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'
