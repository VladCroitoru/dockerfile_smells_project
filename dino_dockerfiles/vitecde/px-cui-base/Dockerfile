FROM php:5.6-fpm
# Install unzip
RUN apt-get update && \
    apt-get install -y unzip git zlib1g-dev python-sphinx rst2pdf rpm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*	

#Install tidy
RUN apt-get update && \
	apt-get -y install libtidy-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*	

#Install required extensions
RUN	docker-php-ext-install zip && \
	docker-php-ext-install tidy

# Configure timezone
RUN echo "date.timezone = UTC" >/usr/local/etc/php/conf.d/defaults.ini && \
    echo "log_errors = On" >>/usr/local/etc/php/conf.d/defaults.ini && \
    echo "upload_max_filesize = 200M" >>/usr/local/etc/php/conf.d/defaults.ini && \
    echo "post_max_size = 200M" >>/usr/local/etc/php/conf.d/defaults.ini && \
    echo "max_input_time = 900" >>/usr/local/etc/php/conf.d/defaults.ini && \
    echo "max_execution_time = 900" >>/usr/local/etc/php/conf.d/defaults.ini && \
    echo "short_open_tag = Off" >>/usr/local/etc/php/conf.d/defaults.ini

WORKDIR /var/www/html/px-cui