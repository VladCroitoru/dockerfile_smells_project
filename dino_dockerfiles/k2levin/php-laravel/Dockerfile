FROM alpine:edge

LABEL MAINTAINER "k2leving@gmail.com"

COPY ./files/.bashrc /root/
COPY ./files/crond/crond /etc/init.d/
COPY ./files/crond/run /run/openrc/s6-scan/crond/
COPY ./files/crond/finish /run/openrc/s6-scan/crond/

RUN apk add --no-cache --update alpine-sdk bash git libpng-dev mysql-client nano nginx nodejs nodejs-npm openrc openssh openssl php7 php7-bcmath php7-ctype php7-curl php7-dom php7-fileinfo php7-fpm php7-gd php7-json php7-mbstring php7-pdo php7-pdo_mysql php7-pecl-redis php7-phar php7-session php7-simplexml php7-tokenizer php7-xml php7-xmlwriter python3 s6 tzdata vim yarn && \
# composer setup
  curl -O https://getcomposer.org/composer.phar && mv composer.phar /usr/local/bin/composer && chmod 755 /usr/local/bin/composer && \
# php-fpm setup
  sed -i 's/user = nobody/user = 1000/1' /etc/php7/php-fpm.d/www.conf && \
# node setup
  npm install -g apidoc bower grunt-cli gulp-cli && \
# openrc setup
  sed -i 's/cgroup_add_service()/cgroup_add_service() { return 0; }\ncgroup_add_service_old()/g' /lib/rc/sh/rc-cgroup.sh && \
  rc-update add s6-svscan default && rc-update add nginx default && rc-update add php-fpm7 default && \
# timezone to UTC+08
  cp /usr/share/zoneinfo/Asia/Singapore /etc/localtime && echo 'Asia/Singapore' > /etc/timezone && apk del tzdata

EXPOSE 80

CMD ["/sbin/init"]
