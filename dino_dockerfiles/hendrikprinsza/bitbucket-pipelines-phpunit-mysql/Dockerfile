FROM debian:jessie-slim
MAINTAINER Hendrik Prinsloo <info@hendrikprinsloo.co.za>

ENV DEBIAN_FRONTEND noninteractive

RUN \
    apt-get update &&\
    apt-get -y --no-install-recommends install locales apt-utils &&\
    apt-get -y --no-install-recommends install ca-certificates git subversion php5-mysqlnd php5-cli php5-sqlite php5-mcrypt php5-curl php5-intl php-gettext php5-json php5-geoip php5-apcu php5-gd php5-imagick php5-xdebug php5-xhprof php5-xmlrpc imagemagick openssh-client curl software-properties-common gettext zip unzip mysql-client apt-transport-https ruby python python3 perl php5-memcached memcached bzip2 wget &&\
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - &&\
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list &&\
    curl -sSL https://deb.nodesource.com/setup_4.x | bash - &&\
    apt-get -y --no-install-recommends install nodejs yarn &&\
    apt-get autoclean && apt-get clean && apt-get autoremove

RUN \
    sed -ri -e "s/^variables_order.*/variables_order=\"EGPCS\"/g" /etc/php5/cli/php.ini &&\
    echo "xdebug.max_nesting_level=250" >> /etc/php5/mods-available/xdebug.ini

RUN \
    apt-get update &&\
    apt-get install -y rsync

RUN \
    curl -sSL https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/bin &&\
    curl -sSL https://phar.phpunit.de/phpunit-5.7.phar -o /usr/bin/phpunit  && chmod +x /usr/bin/phpunit  &&\
    curl -sSL http://codeception.com/codecept.phar -o /usr/bin/codecept && chmod +x /usr/bin/codecept &&\
    npm install --no-color --production --global gulp-cli webpack mocha grunt clean-css-cli uglify-js &&\
    rm -rf /root/.npm /root/.composer /tmp/* /var/lib/apt/lists/*

RUN \
    apt-get update && apt-get install -y --no-install-recommends openjdk-7-jre &&\
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN \
    wget -O sencha-cmd.zip http://cdn.sencha.com/cmd/6.5.1/no-jre/SenchaCmd-6.5.1-linux-amd64.sh.zip &&\
    unzip sencha-cmd.zip && rm sencha-cmd.zip && mv SenchaCmd-6.5.1.*-linux-amd64.sh sencha-cmd.sh && chmod +x sencha-cmd.sh &&\
    mkdir -p /opt/Sencha/Cmd && mv sencha-cmd.sh /opt/Sencha/Cmd &&\
    /opt/Sencha/Cmd/sencha-cmd.sh -q -a
