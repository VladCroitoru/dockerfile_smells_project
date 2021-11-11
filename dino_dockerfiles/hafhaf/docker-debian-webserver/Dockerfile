FROM debian:jessie

RUN \
  apt-get -qq update && \
  apt-get -qq install \
    nginx php5 ssmtp php5-fpm php5-json php5-curl php5-intl php5-recode php5-mcrypt php5-mongo \
    redis-server curl git build-essential gettext-base wget mc nano netcat-openbsd

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install -y nodejs && \
    npm -g install yarn "gulpjs/gulp#4.0" forever pm2 grunt-cli bower redis-commander && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN \
  wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add - && \
  sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' && \
  apt-get update && apt-get -qq install postgresql postgresql-contrib php5-pgsql

RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 &&\
  echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list &&\
  apt-get update && apt-get install -y mongodb-org

COPY startup.sh /startup.sh
COPY tcp-port-wait.sh /tcp-port-wait.sh

EXPOSE 80

CMD ["/bin/bash", "-c", "/startup.sh"]
