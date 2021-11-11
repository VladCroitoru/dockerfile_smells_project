FROM gliderlabs/alpine

# Overall set-up
RUN apk --update --no-cache add \
			curl \
			git \
			mariadb \
			mariadb-client \
			php7-apache2 \
			php7-cli \
			php7-ctype \
			php7-curl \
			php7-dom \
			php7-gd \
			php7-iconv \
			php7-json \
			php7-mbstring \
			php7-opcache \
			php7-openssl \
			php7-pdo_mysql \
			php7-phar \
			php7-tokenizer \
			php7-xml \
      php7-session \
      php7-simplexml \
			&& \
		# Composer
		curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
		# Multirun
		curl -Ls https://github.com/nicolas-van/multirun/releases/download/0.3.0/multirun-alpine-0.3.0.tar.gz | tar -zxv -C /usr/local/bin && \
    # MySQL config
		mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld && \
    # Apache config
		mkdir -p /run/apache2 && chown -R apache:apache /run/apache2 && rm -rf /var/www/localhost && \
    sed -ri \
      -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
      -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
      -e 's#/var/www/localhost/htdocs#/var/www/localhost/web#g' \
      -e 's#AllowOverride None#AllowOverride All#g' \
      -e 's!^#LoadModule rewrite_module!LoadModule rewrite_module!' \
      /etc/apache2/httpd.conf && \
		echo "Success"

# Drupal specific set-up
ENV PATH="/var/www/localhost/vendor/bin/:${PATH}"
# Start with PHP configuration disabled so we don't interfere with Drush
COPY php.ini /etc/php7/php.ini.apache
COPY my.cnf /etc/mysql/my.cnf
COPY ./*.sh /
RUN composer create-project drupal-composer/drupal-project:8.x-dev /var/www/localhost --stability dev --no-dev --no-interaction --no-progress && \
    chmod +x /*.sh && \
    sh /dbinit.sh

WORKDIR /var/www/localhost/
EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]

