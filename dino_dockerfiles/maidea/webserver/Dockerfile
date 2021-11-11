FROM debian:8.2

ENV DEBIAN_FRONTEND noninteractive

# Install php and nginx
RUN apt-get update && apt-get install -y \
    curl \
    git \
    php5-dev \
    php5-cli \
    php5-mysql \
	php5-mcrypt \
    php5-intl \
    php5-curl \
    php5-fpm \
    php-pear \
    nginx





#download and install WKHTMLTOPDF with patched qt (version from web b ecause version in repo does not have "pathed QT")
RUN curl -sS -o wkhtml.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb
#requirements
RUN apt-get install -y fontconfig libxrender1 xfonts-base xfonts-75dpi
RUN dpkg -i wkhtml.deb
RUN rm wkhtml.deb    


#install CRON so we can use scheduler 
# no recomendations because full exim4 is recomended
RUN apt-get --no-install-recommends -y install cron 

# copy crontab config and run crontab daemon
COPY docker-config/cron /etc/cron
RUN crontab /etc/cron




# According to the Docker way, your container should run only one service.
# That�s the whole purpose of using containers after all.
# So, instead of backgrounding your service, you should leave it running in the foreground.
# You basically run one command, thats the sole purpose of your container. A very simple-minded container :)
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer


# Use FPM config files for php config
COPY docker-config/php/fpm.php.ini /etc/php5/fpm/php.ini
COPY docker-config/php/fpm.pool.conf /etc/php5/fpm/pool.d/www.conf

#use nginx site config files
RUN rm /etc/nginx/sites-enabled/*
COPY docker-config/vhosts/* /etc/nginx/sites-enabled/



# Install the server start script
COPY docker-config/start.sh /start.sh
RUN chmod u+x /start.sh

CMD /start.sh
