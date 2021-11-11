FROM nginx:stable-alpine

MAINTAINER JamesJJ@users.noreply.github.com

RUN \
  apk add --no-cache \
  curl \
  bash \
  perl \
  screen \
  perl-html-parser \
  && mkdir -p /var/www

COPY initial.html /var/www/initial.html

COPY conf.d /etc/nginx/conf.d/

WORKDIR /opt/simple_web_status

ADD *.sh ./

CMD [ "bash", "/opt/simple_web_status/run.sh" ]

