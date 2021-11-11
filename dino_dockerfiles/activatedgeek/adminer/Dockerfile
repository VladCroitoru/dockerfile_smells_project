FROM activatedgeek/nginx-php:latest

MAINTAINER Sanyam Kapoor "1sanyamkapoor@gmail.com"

RUN apk update &&\
  apk add curl &&\
  mkdir -p /adminer &&\
  curl -L https://www.adminer.org/latest-en.php > /adminer/index.php &&\
  curl https://raw.githubusercontent.com/vrana/adminer/master/designs/pepa-linha/adminer.css > /adminer/adminer.css &&\
  apk del curl &&\
  rm -rf /etc/nginx/conf.d/* &&\
  rm -rf /var/cache/apk/*

ADD ./nginx/adminer.conf /etc/nginx/conf.d/adminer.conf

EXPOSE 80

ENTRYPOINT ["/usr/bin/supervisord"]
