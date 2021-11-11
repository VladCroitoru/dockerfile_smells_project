FROM phusion/baseimage:0.9.18

# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

ENV HOME /root

RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]

# Nginx-PHP Installation
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y vim curl wget build-essential python-software-properties
RUN add-apt-repository -y ppa:ondrej/php5-5.6
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y --force-yes php5-cli php5-fpm php5-mysql php5-sqlite php5-curl php5-redis php5-memcached \
		       php5-gd php5-mcrypt php5-intl php5-imap php5-tidy php5-dev

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini
RUN sed -i 's/memory_limit\ =\ 128M/memory_limit\ =\ 2G/g' /etc/php5/fpm/php.ini
RUN sed -i 's/\;date\.timezone\ =/date\.timezone\ =\ Asia\/Ho_Chi_Minh/g' /etc/php5/fpm/php.ini
RUN sed -i 's/upload_max_filesize\ =\ 2M/upload_max_filesize\ =\ 200M/g' /etc/php5/fpm/php.ini
RUN sed -i 's/post_max_size\ =\ 8M/post_max_size\ =\ 200M/g' /etc/php5/fpm/php.ini
RUN sed -i 's/max_execution_time\ =\ 30/max_execution_time\ =\ 3600/g' /etc/php5/fpm/php.ini
RUN sed -i 's/\;error_log\ =\ syslog/error_log\ =\ syslog/g' /etc/php5/fpm/php.ini


RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i -e "s/#\sserver_tokens\soff;/server_tokens off;/" /etc/nginx/nginx.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;security.limit_extensions\s*=\s*.php\s*.php3\s*.php4\s*.php5/security.limit_extensions =/g" /etc/php5/fpm/pool.d/www.conf

RUN mkdir -p        /var/www
ADD build/default   /etc/nginx/sites-available/default
RUN mkdir           /etc/service/nginx
ADD build/nginx.sh  /etc/service/nginx/run
RUN chmod +x        /etc/service/nginx/run
RUN mkdir           /etc/service/phpfpm
ADD build/phpfpm.sh /etc/service/phpfpm/run
RUN chmod +x        /etc/service/phpfpm/run

EXPOSE 80
# End Nginx-PHP

# Phalcon-PHP Installation
RUN apt-get install -y git-core gcc autoconf
RUN git clone git://github.com/phalcon/cphalcon.git
RUN cd cphalcon/build && ./install
RUN echo "extension=phalcon.so" >> /etc/php5/fpm/conf.d/30-phalcon.ini
RUN echo "extension=phalcon.so" >> /etc/php5/cli/conf.d/30-phalcon.ini
# End Phalcon-PHP

# Copy source directory to default nginx root directory
ADD www             /var/www

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
