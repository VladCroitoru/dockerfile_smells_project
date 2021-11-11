FROM ubuntu:14.04
MAINTAINER Morgan Blackthorne <morgan@windsofstorm.net>

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/stormerider/rancher-wpmu-nginx-trusty.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.4.8"

# Keep upstart from complaining
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Install NewRelic support
ADD https://download.newrelic.com/548C16BF.gpg /newrelic.gpg
RUN apt-key add /newrelic.gpg
RUN echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list

RUN apt-get update
RUN apt-get -y upgrade

# Basic Requirements
RUN apt-get -y install perlmagick mysql-client nginx php5-fpm php5-mysql php-apc pwgen python-setuptools curl git unzip fcgiwrap php5-curl php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl bzip2 xz-utils zip newrelic-php5

# nginx config
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo "fastcgi_param  SCRIPT_FILENAME    \$document_root\$fastcgi_script_name;" >> /etc/nginx/fastcgi_params
RUN echo "fastcgi_param  PATH_INFO          \$fastcgi_script_name;" >> /etc/nginx/fastcgi_params

# php-fpm config
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/short_open_tag\s*=\s*Off/short_open_tag = On/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php5/fpm/pool.d/www.conf
# Ideally this should be 0660, but until I can track down why www-data can't talk to /var/run/php-fpm.sock, make it 0666
RUN sed -i -e "s/;listen.mode\s*=\s0660/listen.mode = 0666/g" /etc/php5/fpm/pool.d/www.conf
RUN find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;

# nginx site conf
RUN rm /etc/nginx/sites-enabled/default
ADD ./config/nginx-site.conf /etc/nginx/sites-enabled/default

# Supervisor Config
RUN /usr/bin/easy_install supervisor
RUN /usr/bin/easy_install supervisor-stdout
ADD ./config/supervisord.conf /etc/supervisord.conf

# Wordpress Initialization and Startup Script
ADD ./scripts/start.sh /start.sh
RUN chmod 755 /start.sh

# private expose
EXPOSE 80

# volume for mysql database and wordpress install
VOLUME ["/usr/share/nginx/www/"]

CMD ["/bin/bash", "/start.sh"]
