FROM phusion/baseimage:0.9.16
MAINTAINER Bunnyfu <bunnyfu@gmail.com>

# Default baseimage settings
ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
CMD ["/sbin/my_init"]
ENV DEBIAN_FRONTEND noninteractive

# Update software list, install php-nginx & clear cache
RUN curl https://www.dotdeb.org/dotdeb.gpg > dotdeb.gpg
RUN apt-key add dotdeb.gpg
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list
RUN echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y wget nginx php7.0 php7.0-fpm php7.0-cli php7.0-mysql php7.0-opcache php7.0-dev git pkg-config build-essential libmemcached-dev
RUN cd ~/
RUN git clone https://github.com/php-memcached-dev/php-memcached.git
RUN cd php-memcached
RUN git checkout php7
RUN phpize
RUN ./configure --disable-memcached-sasl
RUN make
RUN make install
RUN touch /etc/php/mods-available/memcached.ini
RUN echo "extension=memcached.so" >> /etc/php/mods-available/memcached.ini
RUN ln -s /etc/php/mods-available/memcached.ini /etc/php/7.0/fpm/conf.d/20-memcached.ini
RUN ln -s /etc/php/mods-available/memcached.ini /etc/php/7.0/cli/conf.d/20-memcached.ini

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*

# Configure nginx
RUN echo "daemon off;" >>                                               /etc/nginx/nginx.conf
RUN sed -i "s/sendfile on/sendfile off/"                                /etc/nginx/nginx.conf
RUN mkdir -p                                                            /var/www

# Configure PHP
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"                  /etc/php/7.0/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Kolkata/"        /etc/php/7.0/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g"                 /etc/php/7.0/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"                  /etc/php/7.0/cli/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Kolkata/"        /etc/php/7.0/cli/php.ini

# Add nginx service
RUN mkdir                                                               /etc/service/nginx
ADD build/nginx/run.sh                                                  /etc/service/nginx/run
RUN chmod +x                                                            /etc/service/nginx/run

# Add PHP service
RUN mkdir                                                               /etc/service/phpfpm
ADD build/php/run.sh                                                    /etc/service/phpfpm/run
RUN chmod +x                                                            /etc/service/phpfpm/run

# Add nginx
VOLUME ["/var/www", "/etc/nginx/sites-available", "/etc/nginx/sites-enabled"]

# Workdir
WORKDIR /var/www

EXPOSE 80
