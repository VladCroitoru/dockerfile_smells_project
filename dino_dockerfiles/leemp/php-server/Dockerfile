FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y \
    git \
    curl \
    cron \
    wget \
    zsh \
    nano \
    supervisor \
    nginx \
    php7.0 \
    php7.0-fpm \
    php7.0-cli \
    php7.0-curl \
    php7.0-zip \
    php7.0-json \
    php7.0-mysql \
    php7.0-pgsql \
    php7.0-mcrypt \
    php7.0-mbstring \
    php7.0-gd \
    php7.0-xml \
    mysql-client

RUN apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean

RUN mkdir /run/php/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i "s/display_errors = On/display_errors = Off/" /etc/php/7.0/fpm/php.ini
RUN sed -i "s/post_max_size = 8M/post_max_size = 100M/" /etc/php/7.0/fpm/php.ini
RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 100M/" /etc/php/7.0/fpm/php.ini
RUN sed -i "s/user = www-data/user = root/" /etc/php/7.0/fpm/pool.d/www.conf
RUN sed -i "s/group = www-data/group = root/" /etc/php/7.0/fpm/pool.d/www.conf

# Supervisor conf
RUN echo "[supervisord]" >> /etc/supervisor/supervisord.conf
RUN echo "nodaemon = true" >> /etc/supervisor/supervisord.conf
RUN echo "user = root" >> /etc/supervisor/supervisord.conf

RUN echo "[program:php-fpm7.0]" >> /etc/supervisor/supervisord.conf
RUN echo "command = /usr/sbin/php-fpm7.0 -FR" >> /etc/supervisor/supervisord.conf
RUN echo "autostart = true" >> /etc/supervisor/supervisord.conf
RUN echo "autorestart = true" >> /etc/supervisor/supervisord.conf

RUN echo "[program:nginx]" >> /etc/supervisor/supervisord.conf
RUN echo "command = /usr/sbin/nginx" >> /etc/supervisor/supervisord.conf
RUN echo "autostart = true" >> /etc/supervisor/supervisord.conf
RUN echo "autorestart = true" >> /etc/supervisor/supervisord.conf

RUN echo "[program:cron]" >> /etc/supervisor/supervisord.conf
RUN echo "command = cron -f" >> /etc/supervisor/supervisord.conf
RUN echo "autostart = true" >> /etc/supervisor/supervisord.conf
RUN echo "autorestart = true" >> /etc/supervisor/supervisord.conf


# Install Zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
RUN sed -i "s/robbyrussell/af-magic/" ~/.zshrc
RUN echo TERM=xterm >> /root/.zshrc

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add certbot
# https://certbot.eff.org/
RUN wget -P /usr/sbin/ https://dl.eff.org/certbot-auto
RUN chmod a+x /usr/sbin/certbot-auto

RUN chown -R root:root /etc/cron.d
RUN chmod -R 0644 /etc/cron.d

CMD ["/usr/bin/supervisord"]
