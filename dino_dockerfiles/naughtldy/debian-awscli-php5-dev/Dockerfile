FROM naughtldy/debian-awscli-php5:latest

RUN apt-get update && \

  # phpredis
  apt-get install -y git zip re2c && \
  cd /tmp && \
  wget https://github.com/phpredis/phpredis/archive/3.1.2.zip -O phpredis.zip && \
  unzip -o /tmp/phpredis.zip && \
  mv /tmp/phpredis-* /tmp/phpredis && \
  cd /tmp/phpredis && \
  phpize && \
  ./configure && \
  make && \
  make install && \
  touch /etc/php/5.6/mods-available/redis.ini && \
  echo extension=redis.so > /etc/php/5.6/mods-available/redis.ini && \
  ln -s /etc/php/5.6/mods-available/redis.ini /etc/php/5.6/apache2/conf.d/ && \
  ln -s /etc/php/5.6/mods-available/redis.ini /etc/php/5.6/cli/conf.d/ && \

  # yaml
  apt-get install -y libyaml-dev && \
  pecl install yaml-1.3.0 && \
  echo "extension=yaml.so" >> /etc/php/5.6/mods-available/php.ini && \
  echo "extension=yaml.so" >> /etc/php/5.6/cli/php.ini && \
  # mbstring
  apt-get install -y php5.6-mbstring && \
  echo "extension=php_mbstring.so" >> /etc/php/5.6/mods-available/php.ini && \
  echo "extension=php_mbstring.so" >> /etc/php/5.6/cli/php.ini && \

  # mysql
  apt-get install -y mysql-client && \
  apt-get install -y php5.6-mysql && \

  apt-get clean
