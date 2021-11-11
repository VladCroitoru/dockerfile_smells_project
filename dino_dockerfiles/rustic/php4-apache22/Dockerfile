From ubuntu:precise
MAINTAINER Lee Myers

# Install Apt Utils Apache and Development tools
RUN apt-get update \
    && apt-get install -y \
    apt-utils \
    apache2 \
    apache2-dev \
    bison \
    build-essential \
    libcurl4-openssl-dev \
    libmysqlclient-dev \
    libpng3 \
    libpng3-dev \
    libjpeg-dev \
    file \
    flex \
    wget \
    && ldconfig \
    && rm -r /var/lib/apt/lists/* \
    && service apache2 stop \
    && rm -r /etc/init.d/apache2 

# Download, Compile and Install PHP4
RUN mkdir /tmp/php4 \
    && cd /tmp/php4 \
    && wget http://museum.php.net/php4/php-4.4.9.tar.gz \
    && tar xzf php-4.4.9.tar.gz \
    && cd php-4.4.9 \
    && ./configure \
    --with-apxs2=/usr/bin/apxs2 \
    --with-config-file-path=/etc \
    --with-mysql \
    --with-jpeg-dir=/usr/lib/`uname -i`-linux-gnu \
    --with-png-dir=/usr/lib/`uname -i`-linux-gnu \
    --with-gettext \
    --enable-bcmath \
    --enable-fastcgi \
    --with-tidy \
    --with-curl \
    --with-zlib \
    --with-mysqli \
    --enable-mbstring \
    --enable-mbstr-enc-trans \
    --enable-zend-multibyte \
    && make \
    && make install \
    && cd ~ \
    && rm -rf /tmp/php4

CMD ["apache2ctl", "-D", "FOREGROUND"]

