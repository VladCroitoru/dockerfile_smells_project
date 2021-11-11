FROM ubuntu:14.04

WORKDIR /root
ENV HOME /root

# install basic tools
RUN apt-get update && \
    apt-get install \
    git \
    curl \
    php5 \
    php5-json \
    php5-curl \
    apache2 -y

# install composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

RUN composer create-project ptrofimov/beanstalk_console -s dev /app/src

RUN chown -R www-data:www-data /app

ADD ./apache.conf /etc/apache2/sites-available/000-default.conf

ADD ./start.sh /start.sh

EXPOSE 80

ENTRYPOINT ["/bin/bash"]

CMD ["/start.sh"]
