FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get install -y locales && locale-gen en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=UTF-8
ENV LANG=en_US.UTF-8
ENV TERM xterm

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common \
    && add-apt-repository -y ppa:ondrej/php

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential cron nano git curl supervisor nginx npm ssh \
        php7.1 php7.1-cli php7.1-common php7.1-curl php7.1-json \
        php7.1-xml php7.1-mbstring php7.1-mcrypt php7.1-intl php7.1-fpm php7.1-tidy \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "daemon off;" >> /etc/nginx/nginx.conf \
	&& sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-fpm.conf \
	&& sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.1/fpm/php.ini

COPY nginx/default /etc/nginx/sites-available/default

# Install nodejs
RUN npm install express serve-static

# Install Composer, prestissimo, Satis and Satisfy
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
	&& /usr/local/bin/composer global require hirak/prestissimo \
	&& /usr/local/bin/composer create-project playbloom/satisfy:dev-master --stability=dev \
	&& chmod -R 777 /satisfy \
	&& rm -rf /root/.composer/cache/*

COPY scripts /app/scripts

COPY scripts/crontab /etc/cron.d/satis-cron
COPY config.json /app/config.json
COPY server.js /app/server.js
COPY config.php /satisfy/app/config.php

RUN chmod 0644 /etc/cron.d/satis-cron \
	&& touch /var/log/satis-cron.log \
	&& chmod 777 /app/config.json \
	&& chmod 777 /app/server.js \
	&& chmod +x /app/scripts/startup.sh \
	&& mkdir -p /run/php \
	&& chmod 777 /run/php

COPY supervisor /etc/supervisor/conf.d

WORKDIR /app

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]

EXPOSE 80
