FROM frankhildebrandt/docker-ubuntu-php7-nginx

RUN apt-get update \
 && apt-get install -y php-gd php-xml php-soap php-zip imagemagick \
 && rm -rf /var/lib/apt/lists/* 

RUN curl -O curl -O http://heanet.dl.sourceforge.net/project/typo3/TYPO3%20Source%20and%20Dummy/TYPO3%208.0.1/typo3_src-8.0.1.tar.gz \ 
 && mkdir -p /usr/lib/typo3 \
 && tar xzf typo3_src-8.0.1.tar.gz -C /usr/lib/typo3 \
 && ln -s /usr/lib/typo3/typo3_src-8.0.1 /var/www/html/typo3_src \
 && ln -s typo3_src/index.php /var/www/html/index.php \
 && ln -s typo3_src/typo3 /var/www/html/typo3 \
 && chown -R www-data /var/www \
 && touch /var/www/html/FIRST_INSTALL
 
 RUN echo "max_execution_time=240" >> /etc/php/7.0/fpm/php.ini \
  && echo "max_input_vars=1500" >> /etc/php/7.0/fpm/php.ini
 VOLUME /var/www/html