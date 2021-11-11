FROM nginx:alpine

RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log
RUN mkdir /srv/website

COPY configs/nginx.conf /etc/nginx/conf.d/default.conf

COPY . /srv/website/
