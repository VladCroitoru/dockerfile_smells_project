FROM ubuntu:16.04
LABEL  maintainer "Toro_Unit <mail@torounit.com>"

ENV DEBIAN_FRONTEND noninteractive

# Install library.
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y sudo unzip curl wget git supervisor

# Install Chrome and Node.js.
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update
RUN apt-get install -y chromium-browser
ENV CHROME_PATH /usr/bin/chromium-browser
RUN apt-get install -y nodejs

# Install Noto Sans.
RUN apt-get install -y fonts-noto

# Install PHP.
RUN apt-get install -y php7.0 php7.0-cli php7.0-dev php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-gd php7.0-curl php7.0-zip php-xdebug php-imagick php7.0-fpm

# Install MySQL.
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get install -y nginx mysql-server
RUN usermod -d /var/lib/mysql mysql

# Install WP-CLI.
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN chmod +x wp-cli.phar
RUN mv wp-cli.phar /usr/local/bin/wp

# Install Composer.
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer

# Config nginx.
ADD ./wordpress.conf /etc/nginx/sites-available/wordpress.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/wordpress.conf /etc/nginx/sites-enabled/wordpress.conf
RUN mkdir /var/www/wordpress
RUN chown -R www-data /var/www

# PHP-FPM.
RUN mkdir /run/php
RUN chown www-data /run/php

# Change user www-data.
RUN echo 'www-data ALL=(root) NOPASSWD: ALL' >> /etc/sudoers
USER www-data

# Create Database.
RUN sudo find /var/lib/mysql -type f -exec touch {} \; && sudo service mysql start && \
    sudo mysqladmin create "wordpress" --user="root" --password="root"

# Download WordPress.
WORKDIR /var/www/wordpress
RUN curl -s https://wordpress.org/latest.tar.gz > /tmp/wordpress.tar.gz
RUN tar --strip-components=1 -zxmf /tmp/wordpress.tar.gz -C ./

# Install WordPress.
RUN sudo find /var/lib/mysql -type f -exec touch {} \; && \
    sudo service mysql start && \
    wp config create --dbname=wordpress --dbuser=root --dbpass=root && \
    wp core install \
    --url=http://localhost \
    --title="WP Theme Test Environment" \
    --admin_user="admin" \
    --admin_password="admin" \
    --admin_email="admin@example.com" && \
    wp plugin install https://github.com/WordPress/wordpress-importer/archive/master.zip --activate

# Import Theme Unit Test.
RUN sudo find /var/lib/mysql -type f -exec touch {} \; && \
    sudo service mysql start && \
    curl https://raw.githubusercontent.com/WPTRT/theme-unit-test/master/themeunittestdata.wordpress.xml > /tmp/themeunittestdata.wordpress.xml && \
    wp import /tmp/themeunittestdata.wordpress.xml --authors=create && \
    curl https://raw.githubusercontent.com/jawordpressorg/theme-test-data-ja/master/wordpress-theme-test-date-ja.xml > /tmp/wordpress-theme-test-date-ja.xml && \
    wp import /tmp/wordpress-theme-test-date-ja.xml --authors=create && \
    wp rewrite structure "/%postname%/" && \
    wp option update posts_per_page 5 && \
    wp option update page_comments 1 && \
    wp option update comments_per_page 5 && \
    wp option update show_on_front page && \
    wp option update page_on_front 701  && \
    wp option update page_for_posts 703

# supervisord
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD sudo /usr/bin/supervisord

EXPOSE 80