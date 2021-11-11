FROM php:7.0-fpm
MAINTAINER  Operations <ops@actionstep.com>

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash
RUN apt-get install -y nodejs openssh-client git libcurl4-gnutls-dev libicu-dev \
    libmcrypt-dev libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev \
    libxml2-dev libexpat1-dev libpq-dev libpcre3-dev libtidy-dev libbz2-dev \
    xvfb google-chrome-stable libgconf-2-4 gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi \
    xfonts-75dpi xfonts-scalable x11-apps imagemagick libmagick++-dev zip
RUN pecl install imagick
RUN docker-php-ext-install mcrypt pdo_pgsql intl gd zip bz2
RUN docker-php-ext-enable imagick
RUN curl -L http://static.phpmd.org/php/2.5.0/phpmd.phar > /usr/local/bin/phpmd
RUN curl -L https://github.com/squizlabs/PHP_CodeSniffer/releases/download/2.6.2/phpcs.phar > /usr/local/bin/phpcs
RUN curl -L https://phar.phpunit.de/phpcpd-3.0.1.phar > /usr/local/bin/phpcpd
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN curl -O https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/local/bin/
RUN rm chromedriver_linux64.zip
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install awsebcli
RUN rm get-pip.py
RUN npm install --global gulp-cli eslint eslint-plugin-jsx-a11y eslint-plugin-react \
    stylelint stylelint-config-standard stylelint-scss stylelint-config-sass-guidelines
RUN chmod +x /usr/local/bin/phpmd
RUN chmod +x /usr/local/bin/phpcs
RUN chmod +x /usr/local/bin/phpcpd
RUN chmod +x /usr/local/bin/composer
