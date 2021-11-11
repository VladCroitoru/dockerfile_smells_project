FROM phusion/baseimage:0.9.12

MAINTAINER William Dahlstrom "w.dahlstrom@me.com"

# Ensure UTF-8
RUN locale-gen en_US.UTF-8

# Adding up to date repositories
RUN apt-get -qq update
RUN apt-get -qqy install --no-install-recommends software-properties-common python-software-properties
RUN add-apt-repository -y ppa:ondrej/nginx
RUN add-apt-repository -y ppa:ondrej/php5

# Install nginx, postfix, php5 and dependencies
RUN apt-get -qq update
RUN apt-get -qqy install --force-yes nginx postfix php5-fpm php5-mysql php5-mcrypt php5-curl php5-cli php5-memcache php5-memcached php5-intl curl

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Create www directorys
RUN mkdir -p /var/www

# Set configuration files
ADD conf/nginx.conf /etc/nginx/nginx.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/location/expires.conf /etc/nginx/conf/expires.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/directive-only/x-ua-compatible.conf /etc/nginx/conf/x-ua-compatible.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/location/cross-domain-fonts.conf /etc/nginx/conf/cross-domain-fonts.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/location/protect-system-files.conf /etc/nginx/conf/protect-system-files.conf
ADD https://raw.githubusercontent.com/h5bp/server-configs-nginx/master/h5bp/directive-only/cross-domain-insecure.conf /etc/nginx/h5bp/directive-only/cross-domain-insecure.conf
ADD conf/nginx-site.conf /etc/nginx/sites-available/default
RUN sed -i -e '/access_log/d' /etc/nginx/conf/expires.conf
ADD conf/php.ini /etc/php5/fpm/php.ini
ADD conf/php-fpm.conf /etc/php5/fpm/php-fpm.conf
ADD conf/www.conf /etc/php5/fpm/pool.d/www.conf
ADD conf/main.cf /etc/postfix/main.cf
ADD conf/sasl_passwd /etc/postfix/sasl/sasl_passwd
ADD conf/sysctl.conf /etc/sysctl.conf

# Decouple our data from our container.
VOLUME ["/var/www", "var/log"]

EXPOSE 80
ADD scripts /scripts
RUN chmod +x /scripts/start.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init", "--", "/scripts/start.sh"]
