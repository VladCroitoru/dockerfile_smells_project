FROM php:7.3-fpm-stretch

ENV DEBIAN_FRONTEND=noninteractive

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.22.1.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

RUN \
  	apt-get -y update && \
  	apt-get -y install --no-install-recommends \
  	nginx zip unzip\
	imagemagick webp libmagickwand-dev libyaml-dev \
	python3.6 python3-numpy libopencv-dev python3-setuptools opencv-data \
    gcc nasm build-essential make wget vim git && \
    rm -rf /var/lib/apt/lists/*

#opcache
RUN docker-php-ext-install opcache

#additional libraries
RUN pecl install xdebug imagick yaml-2.2.0 && \
    echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20180731/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini && \
    echo "extension=imagick.so" > /usr/local/etc/php/conf.d/imagick.ini && \
    echo "extension=yaml.so" > /usr/local/etc/php/conf.d/yaml.ini && \
    echo "expose_php=off" > /usr/local/etc/php/conf.d/expose_php.ini

#install MozJPEG
RUN \
    wget "https://github.com/mozilla/mozjpeg/releases/download/v3.2/mozjpeg-3.2-release-source.tar.gz" && \
    tar xvf "mozjpeg-3.2-release-source.tar.gz" && \
    rm mozjpeg-3.2-release-source.tar.gz && \
    cd mozjpeg && \
    ./configure && \
    make && \
    make install

#facedetect script
RUN \
	cd /var && \
    curl https://bootstrap.pypa.io/pip/3.5/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    pip3 install numpy && \
    pip3 install opencv-python && \
    git clone https://github.com/flyimg/facedetect.git && \
    chmod +x /var/facedetect/facedetect && \
    ln -s /var/facedetect/facedetect /usr/local/bin/facedetect

#Smart Cropping pytihon plugin
RUN pip install git+https://github.com/flyimg/python-smart-crop

#composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

#disable output access.log to stdout
RUN sed -i -e 's#access.log = /proc/self/fd/2#access.log = /proc/self/fd/1#g'  /usr/local/etc/php-fpm.d/docker.conf

#copy etc/
COPY resources/etc/ /etc/

ENV PORT 80

COPY resources/docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/docker-entrypoint

WORKDIR /var/www/html

ENTRYPOINT ["docker-entrypoint", "/init"]

