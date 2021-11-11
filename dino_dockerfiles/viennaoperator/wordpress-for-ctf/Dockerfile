FROM visiblevc/wordpress:0.14.0-php7.0

RUN apt-get update && apt-get install -y \
  libfreetype6-dev \
    libmcrypt-dev \
    libpng12-dev \
    libjpeg-dev \
    libpng-dev \
    vim \
    && docker-php-ext-install iconv mcrypt \
    && docker-php-ext-configure gd \
        --enable-gd-native-ttf \
        --with-freetype-dir=/usr/include/freetype2 \
        --with-png-dir=/usr/include \
        --with-jpeg-dir=/usr/include \
    && docker-php-ext-install gd \
    && docker-php-ext-install mbstring \
    && docker-php-ext-enable opcache gd \
    && service apache2 restart

RUN curl \
      -o /run.sh https://raw.githubusercontent.com/viennaoperator/wordpress-for-ctf/master/run.sh \
      && chmod +x /usr/local/bin/wp /run.sh
