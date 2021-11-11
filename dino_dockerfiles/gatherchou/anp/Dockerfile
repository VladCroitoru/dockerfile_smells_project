From alpine

MAINTAINER akira <syuchihin@hotmail.com>

# change aliyun_mirrors with offcial_mirrors
# RUN echo "https://mirrors.aliyun.com/alpine/v3.7/main" > /etc/apk/repositories \ 
# && echo "https://mirrors.aliyun.com/alpine/v3.7/community" >> /etc/apk/repositories \
# && apk update

RUN sed -i "s|5|7|g" /etc/apk/repositories \ 
 && apk update

# install nginx, php
RUN apk add --no-cache nginx \
                       php7 \
                       php7-fpm \
                       php7-openssl \
                       php7-pdo_mysql \
                       php7-mysqli \
                       php7-mbstring \
                       php7-tokenizer \
                       php7-xml \
                       php7-xmlwriter \
                       php7-simplexml \
                       php7-dom \
                       php7-session \
                       php7-ctype \
                       php7-bcmath \
                       php7-json \
                       php7-phar \
                       php7-curl \
                       php7-iconv \
                       php7-mcrypt \
                       libbsd \
 && mkdir -p /run/nginx \
 && mkdir -p /nginx/log /nginx/htdocs \
 && chown -R nginx:nginx /nginx
 
COPY default.conf /etc/nginx/conf.d/default.conf

# set php
RUN sed -i "s|;listen.owner\s*=\s*nobody|listen.owner = nginx|g" /etc/php7/php-fpm.d/www.conf \
 && sed -i "s|;listen.group\s*=\s*nobody|listen.group = nginx|g" /etc/php7/php-fpm.d/www.conf \
 && sed -i "s|;listen.mode\s*=\s*0660|listen.mode = 0660|g" /etc/php7/php-fpm.d/www.conf \
 && sed -i "s|user\s*=\s*nobody|user = nginx|g" /etc/php7/php-fpm.d/www.conf \
 && sed -i "s|group\s*=\s*nobody|group = nginx|g" /etc/php7/php-fpm.d/www.conf \
 && sed -i "s|display_errors\s*=\s*Off|display_errors = On|i" /etc/php7/php.ini \
 && sed -i "s|display_startup_errors\s*=\s*Off|display_startup_errors = On|i" /etc/php7/php.ini \
 && sed -i "s|error_reporting\s*=\s*E_ALL & ~E_DEPRECATED & ~E_STRICT|error_reporting = E_COMPILE_ERROR\|E_RECOVERABLE_ERROR\|E_ERROR\|E_CORE_ERROR|i" /etc/php7/php.ini \ 
 && sed -i "s|;*memory_limit\s*=.*|memory_limit = 512M|i" /etc/php7/php.ini \
 && sed -i "s|;*upload_max_filesize\s*=.*|upload_max_filesize = 50M|i" /etc/php7/php.ini \
 && sed -i "s|;*max_file_uploads\s*=.*|max_file_uploads = 200|i" /etc/php7/php.ini \
 && sed -i "s|;*post_max_size\s*=.*|post_max_size = 100M|i" /etc/php7/php.ini \
 && sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo=0|i" /etc/php7/php.ini

# set timezone
RUN apk add --no-cache tzdata \
 && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
 && echo "Asia/Shanghai" > /etc/timezone

ADD startup.sh /root/startup.sh
RUN chmod +x /root/startup.sh

EXPOSE 80
WORKDIR /nginx/htdocs
CMD ["/root/startup.sh"]