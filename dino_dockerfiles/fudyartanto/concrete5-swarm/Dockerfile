FROM fudyartanto/php-swarm
MAINTAINER arfan@mylits.com

ENV DEBIAN_FRONTEND noninteractive

# install required packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    php5-cli \
    php5-gd \
    php5-mysql \
    php5-curl \
    curl \
    git \
    wget \
    unzip \
  && rm -r /var/lib/apt/lists/*

# use php5 cli instead of php7
RUN rm -rf /usr/bin/php && ln -s /usr/bin/php5 /usr/bin/php
RUN sed -i 's/short_open_tag = Off/; short_open_tag = Off/g' /etc/php/5.6/fpm/php.ini

# install curl
RUN curl -sS -k https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

RUN mkdir /var/www/src
RUN mkdir /src/packages

# install phantomjs
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 --no-check-certificate --output-document=/usr/local/share/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  && tar xjf /usr/local/share/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share \
  && rm /usr/local/share/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  && ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs \
  && ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs \
  && ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs 

# download concrete5
RUN curl -k https://www.concrete5.org/download_file/-/view/81497/8497/ --output /var/www/src/concrete5-5.7.5.zip
RUN unzip /var/www/src/concrete5-5.7.5.zip -d /var/www/src \
  && rm -rf /var/www/src/concrete5-5.7.5.zip \
  && mv /var/www/src/concrete5.7.5 /var/www/src/concrete5-5.7.5 \
  && chmod -R 777 /var/www/src/concrete5-5.7.5/application/files \
  && chmod -R 777 /var/www/src/concrete5-5.7.5/application/config \
  && chmod -R 777 /var/www/src/concrete5-5.7.5/packages
# --------------------------------------------------------------------------------------------------------------
RUN curl -k https://codeload.github.com/concrete5/concrete5/zip/8.1.0 --output /var/www/src/concrete5-8.1.0.zip
RUN unzip /var/www/src/concrete5-8.1.0.zip -d /var/www/src \
  && rm /var/www/src/concrete5-8.1.0.zip \
  && chmod -R 777 /var/www/src/concrete5-8.1.0/application/files \
  && chmod -R 777 /var/www/src/concrete5-8.1.0/application/config \
  && chmod -R 777 /var/www/src/concrete5-8.1.0/packages
# --------------------------------------------------------------------------------------------------------------
RUN curl -k https://codeload.github.com/concrete5/concrete5/zip/8.2.0RC2 --output /var/www/src/concrete5-8.2.0.zip
RUN unzip /var/www/src/concrete5-8.2.0.zip -d /var/www/src \
  && rm /var/www/src/concrete5-8.2.0.zip \
  && mv /var/www/src/concrete5-8.2.0RC2 /var/www/src/concrete5-8.2.0 \
  && chmod -R 777 /var/www/src/concrete5-8.2.0/application/files \
  && chmod -R 777 /var/www/src/concrete5-8.2.0/application/config \
  && chmod -R 777 /var/www/src/concrete5-8.2.0/packages

# install dependencies
# RUN /usr/local/bin/composer install --working-dir=/var/www/src/concrete5-5.7.5/concrete
RUN /usr/local/bin/composer install --working-dir=/var/www/src/concrete5-8.1.0
RUN /usr/local/bin/composer install --working-dir=/var/www/src/concrete5-8.2.0

# create database
RUN /etc/init.d/mysql start \
  && /usr/bin/mysql -u root -padmin -e "CREATE DATABASE concrete5_575" \
  && /usr/bin/mysql -u root -padmin -e "CREATE DATABASE concrete5_810" \
  && /usr/bin/mysql -u root -padmin -e "CREATE DATABASE concrete5_820" \
  # --------------------------------------------------------------------------------------------------------------
  && chmod +x /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:install \
      --db-server=127.0.0.1 \
      --db-username=root \
      --db-password=admin \
      --db-database=concrete5_575 \
      --site=Concrete5-5.7.5 \
      --starting-point=elemental_blank \
      --admin-email=admin@mailinator.com \
      --admin-password=admin \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.debug.display_errors true \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.debug.detail debug \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.cache.blocks false \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.cache.assets false \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.cache.theme_css false \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.cache.overrides false \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.cache.pages false \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.theme.compress_preprocessor_output false \
  && /var/www/src/concrete5-5.7.5/concrete/bin/concrete5 c5:config set concrete.theme.generate_less_sourcemap false \
  # --------------------------------------------------------------------------------------------------------------
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 \
    c5:install \
      --db-server=127.0.0.1 \
      --db-username=root \
      --db-password=admin \
      --db-database=concrete5_810 \
      --site=Concrete5-8.1.0 \
      --starting-point=elemental_blank \
      --admin-email=admin@mailinator.com \
      --admin-password=admin \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.debug.display_errors true \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.debug.detail debug \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.cache.blocks false \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.cache.assets false \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.cache.theme_css false \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.cache.overrides false \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.cache.pages false \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.theme.compress_preprocessor_output false \
  && /var/www/src/concrete5-8.1.0/concrete/bin/concrete5 c5:config set concrete.theme.generate_less_sourcemap false \
  # --------------------------------------------------------------------------------------------------------------
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 \
    c5:install \
      --db-server=127.0.0.1 \
      --db-username=root \
      --db-password=admin \
      --db-database=concrete5_820 \
      --site=Concrete5-8.2.0 \
      --starting-point=elemental_blank \
      --admin-email=admin@mailinator.com \
      --admin-password=admin \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.debug.display_errors true \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.debug.detail debug \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.cache.blocks false \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.cache.assets false \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.cache.theme_css false \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.cache.overrides false \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.cache.pages false \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.theme.compress_preprocessor_output false \
  && /var/www/src/concrete5-8.2.0/concrete/bin/concrete5 c5:config set concrete.theme.generate_less_sourcemap false

RUN ln -s /var/www/src/concrete5-5.7.5 /var/www/html/php5.6 \
  # && ln -s /var/www/src/concrete5-5.7.5 /var/www/html/php7.0 \ concrete5-5.7.5 have couple of issues i php7
  # --------------------------------------------------------------------------------------------------------------
  && ln -s /var/www/src/concrete5-8.1.0 /var/www/html/php5.6 \
  && ln -s /var/www/src/concrete5-8.1.0 /var/www/html/php7.0 \
  # --------------------------------------------------------------------------------------------------------------
  && ln -s /var/www/src/concrete5-8.2.0 /var/www/html/php5.6 \
  && ln -s /var/www/src/concrete5-8.2.0 /var/www/html/php7.0

RUN rm -rf /var/www/src/concrete5-5.7.5/packages \
  && rm -rf /var/www/src/concrete5-8.1.0/packages \
  && rm -rf /var/www/src/concrete5-8.2.0/packages \
  && ln -s /src/packages /var/www/src/concrete5-5.7.5 \
  && ln -s /src/packages /var/www/src/concrete5-8.1.0 \
  && ln -s /src/packages /var/www/src/concrete5-8.2.0

RUN chmod -R 777 /var/www/src/concrete5-5.7.5/application/files \
  && chmod -R 777 /var/www/src/concrete5-5.7.5/application/config \
  && chmod -R 777 /var/www/src/concrete5-5.7.5/packages \
  # --------------------------------------------------------------------------------------------------------------
  && chmod -R 777 /var/www/src/concrete5-8.1.0/application/files \
  && chmod -R 777 /var/www/src/concrete5-8.1.0/application/config \
  && chmod -R 777 /var/www/src/concrete5-8.1.0/packages \
  # --------------------------------------------------------------------------------------------------------------
  && chmod -R 777 /var/www/src/concrete5-8.2.0/application/files \
  && chmod -R 777 /var/www/src/concrete5-8.2.0/application/config \
  && chmod -R 777 /var/www/src/concrete5-8.2.0/packages

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 8643

CMD ["/usr/bin/supervisord"]