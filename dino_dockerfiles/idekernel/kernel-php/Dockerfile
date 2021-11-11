FROM idekernel/php
#COPY docker-php-source docker-php-ext-* docker-php-entrypoint /usr/local/bin/
RUN apt-get update && apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng12-dev \
		wget \
		vim \
		git \
	&& docker-php-ext-install -j$(nproc) iconv mcrypt \
        && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd
	
#install zeromq
RUN wget --quiet https://github.com/zeromq/libzmq/releases/download/v4.2.1/zeromq-4.2.1.tar.gz \
	&& tar zxf zeromq-4.2.1.tar.gz \
	&& cd zeromq-4.2.1 \
	&& ./configure --prefix=/usr/local/zeromq \
	&& make \
	&& make install
#install php-zmq
#RUN mkdir -p /usr/src/php/ext
RUN docker-php-source extract
RUN git clone https://github.com/mkoppanen/php-zmq.git \
	&& mv php-zmq/ /usr/src/php/ext/ \
	&& docker-php-ext-configure php-zmq --with-php-config=/usr/local/bin/php-config  --with-zmq=/usr/local/zeromq \
	&& docker-php-ext-install -j$(nproc) php-zmq \
	&& docker-php-source delete

RUN curl -sS https://getcomposer.org/installer | php \
        && mv composer.phar /usr/local/bin/composer
RUN wget --quiet https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar \
    && php ./jupyter-php-installer.phar install
RUN rm -Rf *
USER $NB_USER
