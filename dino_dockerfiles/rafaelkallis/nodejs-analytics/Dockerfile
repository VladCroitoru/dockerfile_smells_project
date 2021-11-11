FROM rafaelkallis/alpine-node-nginx

MAINTAINER Rafael Kallis <rk@rafaelkallis.com>

COPY app /tmp/app
COPY package.json /tmp
COPY brunch-config.js /tmp

RUN cd /tmp \
    && npm install \
    && npm install brunch -g \
    && npm run prod \
    && mv public/* /usr/share/nginx/html \
    && cd / \
    && rm -r /tmp/*

EXPOSE 80