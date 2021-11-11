FROM occitech/cakephp:5.6-apache

ADD https://github.com/prashants/webzash/releases/download/v2.6/webzash-v2.6.tar.gz /tmp/webzash.tar.gz
RUN tar -xzf /tmp/webzash.tar.gz -C /var/www/html --strip 1

RUN echo "RewriteEngine on\\n" > /var/www/html/.htaccess
RUN echo "RewriteRule . index.php [L]\\n" >> /var/www/html/.htaccess

COPY ./* /var/www/html/