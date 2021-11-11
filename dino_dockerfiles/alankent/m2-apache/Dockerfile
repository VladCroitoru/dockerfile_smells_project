FROM php:7.0-apache
MAINTAINER Alan Kent <alan.james.kent@gmail.com>


########### Apache and PHP Setup ########### 

# Get a good version of PHP with extensions installed,
# Add some more useful utlities,
# Enable Apache rewrite module.

RUN apt-get update \
 && apt-get install -y libfreetype6-dev libicu-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev libxslt1-dev \
 && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
 && docker-php-ext-install gd intl mbstring mcrypt pdo_mysql xsl zip \
 && apt-get update \
 && apt-get install -y vim git curl net-tools telnet sudo cron zip \
 && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
 && a2enmod rewrite \
 && echo "memory_limit = 2048M" > /usr/local/etc/php/php.ini

# Environment variables from /etc/apache2/apache2.conf
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid


########### SSHD ########### 

# Enable sftp
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir -p /var/run/sshd
EXPOSE 22


########### MySQL Setup ########### 

env MYSQL_ROOT_PASSWORD=magento2
env MYSQL_DATABASE=magento2
env MYSQL_USER=magento2
env MYSQL_PASSWORD=magento2
env MYSQL_ALLOW_EMPTY_PASSWORD=yes

ADD mysql-install.sh /usr/local/bin
RUN chmod +x /usr/local/bin/mysql-install.sh
RUN /usr/local/bin/mysql-install.sh

# Create the 'magento2' database
ADD mysql-init.sh /usr/local/bin
RUN chmod +x /usr/local/bin/mysql-init.sh
RUN /usr/local/bin/mysql-init.sh mysqld


########### Magento Setup ########### 

# We don't install any code here, but we set up an account to own
# it so other images don't have to repeat all this configuration.

ENV MAGENTO_USER magento
ENV MAGENTO_PASSWORD magento
ENV MAGENTO_GROUP magento

ENV APACHE_RUN_USER magento
ENV APACHE_RUN_GROUP magento

ENV MAGENTO_REPO_USERNAME ""
ENV MAGENTO_REPO_PASSWORD ""

# Add the Apache virtual host file
RUN rm /etc/apache2/sites-enabled/*
ADD apache_default_vhost /etc/apache2/sites-enabled/magento.conf

# Create a 'magento' account with password 'magento' to own the source files.
# Run Apache as user 'magento' as well.
RUN useradd -m -s /bin/bash -p $(openssl passwd -1 ${MAGENTO_PASSWORD}) -G sudo ${MAGENTO_USER}

# Don't ask for passwords when running sudo.
RUN echo "magento ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Overwrite apache config file to use /magento2 instead of /var/www/html
ADD apache2.conf /etc/apache2/apache2.conf


# Fix up file permissions.
# Load the database with Luma.
# Run cron jobs to update indexes etc.
# Bashrc file.
RUN sed -i -e 's/www-data/magento/g' /etc/apache2/envvars \
 && sed -i -e 's/www-data/magento/g' /etc/apache2/apache2.conf \
 && sudo -u ${MAGENTO_USER} sh -c "echo 'export PATH=\${PATH}:/magento2/bin' >> /home/magento/.bashrc" \
 && sudo -u ${MAGENTO_USER} sh -c "echo 'PS1=m2$\ ' >> /home/magento/.bashrc" \
 && echo 'if [ $PPID == 0 ]; then exec sudo -u magento bash ; fi' >> /root/.bashrc


########### Unison file syncing ########### 

# Unison 2.40.102 - http://www.seas.upenn.edu/~bcpierce/unison//download/releases/unison-2.40.102/
# http://unison-binaries.inria.fr/
#RUN apt-get update && apt-get install -y unison

# Unison 2.48.3
# Linux:    https://github.com/TentativeConvert/Syndicator/blob/master/unison-binaries/unison-2.48.3
# Windows:  https://www.irif.fr/~vouillon/unison/ - HTML pages listing downloads.
#           https://www.irif.fr/~vouillon/unison/unison%202.48.3.zip - binaries
# Mac OS X: http://unison-binaries.inria.fr/index.html#OSX - HTML page
#           http://unison-binaries.inria.fr/files/Unison-OS-X-2.48.3.zip - binaries
RUN cd /usr/local/bin \
 && curl -L -o unison https://github.com/TentativeConvert/Syndicator/raw/master/unison-binaries/unison-2.48.3 \
 && curl -L -o unison-fsmonitor https://github.com/TentativeConvert/Syndicator/raw/master/unison-binaries/unison-fsmonitor \
 && chmod +x unison unison-fsmonitor

RUN mkdir /windows \
 && cd /windows \
 && curl -L -o unison-windows.zip https://www.irif.fr/~vouillon/unison/unison%202.48.3.zip \
 && unzip unison-windows.zip \
 && rm unison-windows.zip \
 && mv 'unison 2.48.3 text.exe' unison.exe \
 && rm 'unison 2.48.3 GTK.exe' \
 && chown -R ${MAGENTO_USER}:${MAGENTO_GROUP} .

RUN mkdir /mac-osx \
 && cd /mac-osx \
 && curl -L -o unison-mac-osx.zip http://unison-binaries.inria.fr/files/Unison-OS-X-2.48.3.zip \
 && unzip unison-mac-osx.zip \
 && rm unison-mac-osx.zip \
 && chown -R ${MAGENTO_USER}:${MAGENTO_GROUP} .

# Unison 2.48.3 (from internet searches, but comes up with 404 errors)
#RUN apt-get update && apt-get install -y software-properties-common python-software-properties
#RUN add-apt-repository ppa:eugenesan/ppa && apt-get update && apt-get install -y unison

# Unison from source code (but does not compile)
#RUN apt-get update \
# && apt-get install -y ocaml \
# && mkdir /tmp/unison \
# && cd /tmp/unison \
# && curl -O http://www.seas.upenn.edu/~bcpierce/unison//download/releases/stable/unison-2.48.4.tar.gz \
# && tar zxvf unison-2.48.4.tar.gz \
# && cd src \
# && ls -l \
# && make UISTYLE=text NATIVE=false \
# && cp unison /usr/local/bin/ \
# && cd /tmp \
# && rm -rf /tmp/unison


########### NodeJS ########### 

# Install NodeJS (after curl is installed above).
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \
 && apt-get update \
 && apt-get install -y nodejs


########### Gulp and Frontool ########### 

# Coming soon - Needs review against current version of Frontool.

# Install Gulp
#ADD gulp-snowdogapps /gulp
#ADD run-gulp.sh /usr/local/bin
#RUN chown magento:magento /usr/local/bin/run-gulp.sh \
# && chmod +rx /usr/local/bin/run-gulp.sh \
# && chown -R magento:magento /gulp \
# && cd /gulp \
# && npm install -g gulp \
# && npm install --save-dev gulp \
# && npm install jshint gulp-less gulp-concat gulp-uglify gulp-rename gulp-livereload gulp-sourcemaps gulp-util notify-send --save-dev \
# && npm install \
# && chown -R magento:magento .
#EXPOSE 3000
#EXPOSE 3001


########### Set working directory and PATH ########### 

WORKDIR /magento2
ENV SHELL /bin/bash
ENV PATH PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/magento2/bin

