FROM debian:jessie

RUN apt-get update
RUN apt-get install -y nginx curl exiftran imagemagick
RUN apt-get install -y php5-dev php5-imagick php5-mysql php5-fpm php5-curl php5-gd php5-mcrypt php-pear
RUN pecl install oauth && mkdir -p /etc/php5/conf.d && echo 'extension=oauth.so' >> /etc/php5/conf.d/oauth.ini

WORKDIR /trovebox

ADD https://github.com/photo/frontend/archive/4.0.0-rc5.tar.gz /tmp/trovebox.tar.gz
RUN tar -zxf /tmp/trovebox.tar.gz -C /trovebox --strip 1

RUN mkdir src/userdata src/html/photos src/html/assets/cache
RUN chown www-data:www-data src/userdata src/html/photos src/html/assets/cache

RUN sed -i '/server_name/d' src/configs/openphoto-nginx.conf
RUN sed -i '/fastcgi_pass 127.0.0.1:9000;/d' src/configs/openphoto-nginx.conf
RUN sed -i 's/root.*yourdomain.com.*;/root \/trovebox\/src\/html;/' src/configs/openphoto-nginx.conf
RUN sed -i 's/#fastcgi_pass fastcgi_pass/fastcgi_pass/' src/configs/openphoto-nginx.conf

RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /trovebox/src/configs/openphoto-nginx.conf /etc/nginx/sites-enabled/trovebox
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf

RUN sed -i 's/^file_uploads = .*/file_uploads = On/' /etc/php5/fpm/php.ini
RUN sed -i 's/^upload_max_filesize = .*/upload_max_filesize = 16M/' /etc/php5/fpm/php.ini
RUN sed -i 's/^post_max_size = .*/post_max_size = 16M/' /etc/php5/fpm/php.ini

EXPOSE 80
CMD service php5-fpm start && nginx
