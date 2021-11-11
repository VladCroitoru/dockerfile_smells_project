FROM debian:stretch-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y php7.0-fpm php7.0-ldap php7.0-mysql php7.0-gd php7.0-mcrypt graphviz php7.0-curl php7.0-zip php7.0-xml php7.0-soap php-apcu php7.0-mbstring
RUN apt-get clean && rm -rf /var/lib/apt

# Add image configuration and scripts
ADD run.sh /run.sh
RUN chmod u+x /run.sh

# Add php7.0-fpm specific configuration
ADD www.conf /etc/php/7.0/fpm/pool.d/www.conf

# Create php run folder

RUN mkdir /run/php

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

expose 9001
CMD ["/run.sh"]
