FROM idfly/php-app

RUN apt-get update
RUN apt-get install -y \
  npm \
  libpng12-dev \
  libjpeg62-turbo-dev \
  libfreetype6-dev \
  libmcrypt-dev \
  zip

RUN docker-php-ext-install -j$(nproc) iconv mcrypt \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd

RUN npm install uglify-js -g

RUN ln -s /usr/bin/nodejs /usr/bin/node