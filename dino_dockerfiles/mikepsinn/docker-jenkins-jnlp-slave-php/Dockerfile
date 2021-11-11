FROM jenkinsci/jnlp-slave:latest
MAINTAINER Baptiste Gaillard <baptiste.gaillard@gomoob.com>

# see https://github.com/phpbrew/phpbrew-container
USER root

ENV COMPOSER_VERSION=1.4.2 \
    PHPMD_VERSION=2.6.0 \
    PHPUNIT_VERSION=6.2.3 \
    PHPBREW_ROOT=/home/jenkins/.phpbrew \
    PHPBREW_HOME=/home/jenkins/.phpbrew \
    PHPBREW_SET_PROMPT=1 \
    PHPBREW_PHP=php-7.1.7

RUN printf "\n\n==== Install utility tools and libraries ====\n" \
 && apt-get update \
 && apt-get install -y apt-utils automake gcc g++ make lcov libbz2-dev libcurl4-openssl-dev libedit-dev libedit2 \
                       libgmp-dev libgmp3-dev libjpeg-dev libicu-dev libmcrypt-dev libpng12-dev libreadline-dev \
                       libsasl2-dev libssl-dev libtidy-dev libxml2 libxml2-dev libxml2-utils libxslt1-dev mediainfo \
                       openssl pkg-config systemtap-sdt-dev postgresql-server-dev-all \

 && printf "\n\n==== Install PHP (required to install phpbrew after ====\n" \
 && echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list \
 && wget -O- https://www.dotdeb.org/dotdeb.gpg | apt-key add - \
 && apt update \
 && apt install -y php7.0 php7.0-dev php7.0-fpm php7.0-mysql php7.0-curl php7.0-json php7.0-gd php7.0-mcrypt \
                   php7.0-msgpack php7.0-memcached php7.0-intl php7.0-sqlite3 php7.0-gmp php7.0-geoip php7.0-mbstring \
                   php7.0-xml php7.0-zip mysql-client mysql-server \

 && printf "\n\n==== Install PHP tools ====\n" \
 && mkdir -p /usr/bin \
 && wget -q -O /usr/bin/phpunit https://phar.phpunit.de/phpunit-$PHPUNIT_VERSION.phar && chmod +x /usr/bin/phpunit \
 && wget -q -O /usr/bin/composer https://getcomposer.org/download/$COMPOSER_VERSION/composer.phar && chmod +x /usr/bin/composer \
 && wget -q -O /usr/bin/phpmd http://static.phpmd.org/php/$PHPMD_VERSION/phpmd.phar && chmod +x /usr/bin/phpmd \
 && wget -q -O /usr/bin/sami http://get.sensiolabs.org/sami.phar && chmod +x /usr/bin/sami \
 && wget -q -O /usr/bin/phpcov https://phar.phpunit.de/phpcov.phar && chmod +x /usr/bin/phpcov \
 && wget -q -O /usr/bin/phpcpd https://phar.phpunit.de/phpcpd.phar && chmod +x /usr/bin/phpcpd \
 && wget -q -O /usr/bin/phploc https://phar.phpunit.de/phploc.phar && chmod +x /usr/bin/phploc \
 && wget -q -O /usr/bin/phptok https://phar.phpunit.de/phptok.phar && chmod +x /usr/bin/phptok \
 && wget -q -O /usr/bin/box https://github.com/box-project/box2/releases/download/2.5.2/box-2.5.2.phar && chmod +x /usr/bin/box \

 && printf "\n\n==== Install phpbrew ====\n" \
 && curl -L -O https://github.com/phpbrew/phpbrew/raw/master/phpbrew \
 && chmod +x phpbrew \
 && mv phpbrew /usr/bin \

 && printf "\n\n==== Install Node ====\n" \
 && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
 && apt-get install -y nodejs \

 && printf "\n\n==== Install Yarn ====\n" \
 && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
 && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
 && apt-get update && apt-get install -y yarn \

 && printf "\n\n==== Install Grunt ====\n" \
 && npm install -g grunt-cli

USER jenkins

RUN printf "\n\n==== Install prestissimo ====\n" \
 && composer global require hirak/prestissimo \

 # see https://wiki.gentoo.org/wiki/GCC_optimization/fr
 # see https://wiki.gentoo.org/wiki/Safe_CFLAGS
 # see https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html
 # see https://github.com/mgorny/cpuid2cpuflags
 # CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3
 #                -maes -mavx -mavx2 -mf16c -mfma -mmmx -mpopcnt -msse -msse2 -msse3 -msse4.1 -msse4.2 -mssse3
 # WARNING: Will generate code which will only work under Amazon t2 instances !
 && printf "\n\n==== Install several PHP versions with phpbrew ====\n" \
 && export CFLAGS="-march=sandybridge -O3" \
 && export CXXFLAGS="${CFLAGS}" \
 && phpbrew init \
 && echo 'source /home/jenkins/.phpbrew/bashrc' >> /home/jenkins/.bashrc \
 && phpbrew install -j $(nproc) 7.0.21 +everything -debug -dtrace -gcov -gmp -phpdbg -zts -- \
 --with-libdir=lib/x86_64-linux-gnu --with-gd=shared --enable-gd-natf --with-jpeg-dir=/usr --with-png-dir=/usr \
 && phpbrew install -j $(nproc) 7.1.7 +everything -debug -dtrace -gcov -gmp -phpdbg -zts -- \
 --with-libdir=lib/x86_64-linux-gnu --with-gd=shared --enable-gd-natf --with-jpeg-dir=/usr --with-png-dir=/usr \

 && printf "\n\n==== Install PHP extensions for PHP 7.0.21 ====\n" \
 && export PHPBREW_PHP=php-7.0.21 \
 && phpbrew switch 7.0.21 \
 && phpbrew ext install --downloader wget xdebug  latest && phpbrew ext clean xdebug \
 && phpbrew ext install --downloader wget apcu    latest && phpbrew ext clean apcu \
 && phpbrew ext install --downloader wget apcu_bc latest && phpbrew ext clean apcu_bc \
 && phpbrew ext install --downloader wget mongodb latest && phpbrew ext clean mongodb \

 && printf "\n\n==== Install PHP extensions for PHP 7.1.7 ====\n" \
 && export PHPBREW_PHP=php-7.1.7 \
 && phpbrew switch 7.1.7 \
 && phpbrew ext install --downloader wget xdebug  latest && phpbrew ext clean xdebug \
 && phpbrew ext install --downloader wget apcu    latest && phpbrew ext clean apcu \
 && phpbrew ext install --downloader wget apcu_bc latest && phpbrew ext clean apcu_bc \
 && phpbrew ext install --downloader wget mongodb latest && phpbrew ext clean mongodb \

 && phpbrew clean php-7.0.21 \
 && phpbrew clean php-7.1.7 \

# Update PHP ini file names to enforce loading in a specific order
 && rm $PHPBREW_HOME/php/php-7.0.21/var/db/* \
 && rm $PHPBREW_HOME/php/php-7.1.7/var/db/* \

 && printf "\n\n==== Configure global PHP configuration parameters ====\n" \
 && sed -i 's/memory_limit = 128M/memory_limit = -1/g' $PHPBREW_HOME/php/php-7.0.21/etc/php.ini \
 && sed -i 's/memory_limit = 128M/memory_limit = -1/g' $PHPBREW_HOME/php/php-7.1.7/etc/php.ini

COPY ini/* $PHPBREW_HOME/php/php-7.0.21/var/db/
COPY ini/* $PHPBREW_HOME/php/php-7.1.7/var/db/

USER root
RUN chown jenkins:jenkins $PHPBREW_HOME/php/php-7.0.21/var/db/* \
 && chown jenkins:jenkins $PHPBREW_HOME/php/php-7.1.7/var/db/*
USER jenkins

# For unknown reasons we encounter the following XDebug loading error, so we manually copy the XDebug library
#  "Failed loading /usr/lib/php/20151012/xdebug.so:  /usr/lib/php/20151012/xdebug.so: cannot open shared object file: \
#   No such file or directory"
RUN echo "zend_extension=$PHPBREW_HOME/php/php-7.0.21/lib/php/extensions/no-debug-non-zts-20151012/xdebug.so" \
    > $PHPBREW_HOME/php/php-7.0.21/var/db/10-xdebug.ini \
 && echo "zend_extension=$PHPBREW_HOME/php/php-7.1.7/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so" \
    > $PHPBREW_HOME/php/php-7.1.7/var/db/10-xdebug.ini

# Create aliases to call PHP more easyly
COPY php/php* /usr/bin/

# Add execution rights to php
USER root
RUN chmod +x /usr/bin/php*
USER jenkins

ENTRYPOINT ["jenkins-slave"]
