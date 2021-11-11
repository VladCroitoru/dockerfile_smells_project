FROM debian:jessie
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>

# Install Requirment
# - Postgresql key ACCC4CF8
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ACCC4CF8 \
 && echo "deb http://mirror.leaseweb.net/debian/ stable main\ndeb http://mirror.leaseweb.net/debian/ jessie-updates main\ndeb http://security.debian.org/ jessie/updates main" > /etc/apt/sources.list \
 && echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" >> /etc/apt/sources.list.d/postgresql.list \
 && apt-get update \
 && DEBCONF_FRONTEND=noninteractive apt-get install -y curl sudo zsh git zip dnsutils mlocate logrotate locales nano \
                        nginx openssh-server postgresql-client postgresql \
                        php5-cli php5-curl php-pear php5-dev php5-fpm php5-gd php5-mcrypt php5-intl php5-pgsql php5-redis php5-xdebug php5-xsl \
 && rm -rf /var/lib/apt/lists/*

# Add & config hurad user
RUN echo "hurad ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
 && useradd --create-home --user-group -s /usr/bin/zsh hurad \
 && echo "hurad:hurad"|chpasswd \
 && sudo -u hurad -H sh -c "export SHELL=/usr/bin/zsh; curl -L http://install.ohmyz.sh | bash" \
 && sudo -u hurad -H sh -c "sed -i 's/ZSH_THEME=\".*\"/ZSH_THEME=\"maran\"/g' /home/hurad/.zshrc"

# Install Adminer
RUN mkdir -p /srv/tools/adminer \
 && cd /srv/tools/adminer \
 && curl -SLO http://www.adminer.org/latest.php \
 && curl -SLO https://raw.githubusercontent.com/pappu687/adminer-theme/master/adminer.css \
 && curl -SLO https://raw.githubusercontent.com/pappu687/adminer-theme/master/adminer-bg.png \
 && mv latest.php index.php

# Install phpPgAdmin
RUN mkdir -p /srv/tools/phppgadmin \
 && cd /srv/tools/phppgadmin \
 && git clone git://github.com/phppgadmin/phppgadmin.git . \
 && mv conf/config.inc.php-dist conf/config.inc.php \
 && sed -i "s/$conf\['extra_login_security'\] = true/$conf\['extra_login_security'\] = false/g" conf/config.inc.php

# PHP Config
RUN cp /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/\[www\]/\[hurad\]/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/user = www-data/user = hurad/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/group = www-data/group = hurad/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/listen = \/var\/run\/php5-fpm.sock/listen = \/var\/run\/php5-fpm-hurad.sock/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/listen.owner = www-data/listen.owner = hurad/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/listen.group = www-data/listen.group = hurad/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/;listen.mode = 0660/listen.mode = 0666/g" /etc/php5/fpm/pool.d/hurad.conf \
 && sed -i "s/;date.timezone =/date.timezone = Asia\/Tehran/g" /etc/php5/fpm/php.ini \
 && sed -i "s/;date.timezone =/date.timezone = Asia\/Tehran/g" /etc/php5/cli/php.ini \
 && sed -i "s/upload_max_filesize = .*/upload_max_filesize = 12M/g" /etc/php5/fpm/php.ini \
 && sed -i "s/post_max_size = .*/post_max_size = 128M/g" /etc/php5/fpm/php.ini

# Config Nginx
COPY ./assets/configs/nginx/default /etc/nginx/sites-available/
COPY ./assets/configs/nginx/hurad /etc/nginx/sites-enabled/

# Add init script
COPY ./assets/init.sh /opt/
RUN chmod a+x /opt/init.sh

WORKDIR /srv/www
ENTRYPOINT ["/opt/init.sh"]
CMD ["start"]

EXPOSE 80 8080 443 5432
