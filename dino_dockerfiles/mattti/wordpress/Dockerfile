FROM wordpress:latest
MAINTAINER Mathias Henrich <wordpress@henrich.eu>
RUN { \
             echo 'safe_mode = Off'; \
             echo 'file_uploads = On'; \
             echo 'memory_limit = 256M'; \
             echo 'upload_max_filesize = 256M'; \
             echo 'post_max_size = 300M'; \
             echo 'max_execution_time = 600'; \ 
        } > /usr/local/etc/php/conf.d/custom.ini
RUN a2enmod remoteip
RUN a2enmod headers
COPY mydocker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["mydocker-entrypoint.sh"]
CMD ["apache2-foreground"]