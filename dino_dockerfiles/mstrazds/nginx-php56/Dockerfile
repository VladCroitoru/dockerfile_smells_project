FROM phusion/baseimage:0.9.22

# Phusion setup
ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]

# Set terminal to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Nginx-PHP Installation
RUN apt-get update -y && apt-get install -y wget build-essential python-software-properties git-core vim nano
RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \
	echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 4F4EA0AAE5267A6C
RUN add-apt-repository -y ppa:ondrej/php && add-apt-repository -y ppa:nginx/stable
RUN apt-get update -y && apt-get upgrade -y && apt-get install -q -y php5.6 php5.6-dev php5.6-fpm php5.6-mysqlnd \
	php5.6-pgsql php5.6-curl php5.6-gd php5.6-mbstring php5.6-mcrypt php5.6-intl php5.6-imap php5.6-tidy \
	php5.6-xml php5.6-xmlrpc zip unzip php5.6-zip newrelic-php5 nginx-full ntp

# Create new symlink to UTC timezone for localtime
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/UTC /etc/localtime

# Update PECL channel listing
RUN pecl channel-update pecl.php.net

# Add build script
RUN mkdir -p /root/setup
ADD build/setup.sh /root/setup/setup.sh
RUN chmod +x /root/setup/setup.sh
RUN (cd /root/setup/; /root/setup/setup.sh)

# Copy files from repo
ADD build/default /etc/nginx/sites-available/default
ADD build/nginx.conf /etc/nginx/nginx.conf
ADD build/php-fpm.conf /etc/php/5.6/fpm/php-fpm.conf
ADD build/www.conf /etc/php/5.6/fpm/pool.d/www.conf
ADD build/.bashrc /root/.bashrc

# Add startup scripts for services
ADD build/nginx.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run

ADD build/phpfpm.sh /etc/service/phpfpm/run
RUN chmod +x /etc/service/phpfpm/run

ADD build/ntp.sh /etc/service/ntp/run
ADD build/ntp.conf /etc/ntp.conf
RUN chmod +x /etc/service/ntp/run

# Set WWW public folder
RUN mkdir -p /var/www/public
ADD www/index.php /var/www/public/index.php

RUN chown -R www-data:www-data /var/www
RUN chmod -R 755 /var/www

# Add New Relic APM install script
RUN mkdir -p /etc/my_init.d
ADD build/newrelic.sh /etc/my_init.d/newrelic.sh
RUN chmod +x /etc/my_init.d/newrelic.sh

# Setup environment variables for initializing New Relic APM
ENV NR_INSTALL_SILENT 1
ENV NR_INSTALL_KEY **ChangeMe**
ENV NR_APP_NAME "Docker PHP Application"

# Set terminal environment
ENV TERM=xterm

# Port and settings
EXPOSE 80

# Cleanup apt and lists
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
