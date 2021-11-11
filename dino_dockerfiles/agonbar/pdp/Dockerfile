FROM debian

# Install all necessary software
RUN apt update && apt dist-upgrade -y && \
apt install apache2 vim mysql-server php php-pear php-mysql php-intl php-mbstring curl ssh zip -y

# Create iu user and give pèrmission
RUN useradd -ms /bin/bash iu && echo "iu:iu" | chpasswd && chown iu:iu /var/www/html && chown iu:iu /var/www/html
WORKDIR /var/www/html
USER iu

# Install CakePHP and configure it
RUN curl -s https://getcomposer.org/installer | php
RUN php composer.phar create-project --prefer-dist cakephp/app lamorisse | cat -
USER root
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf

# Prepare Database with permission
RUN echo "CREATE USER 'iu'@'localhost' IDENTIFIED BY 'iu';" > dbStart.dump && \
echo "CREATE DATABASE iu;" >> dbStart.dump && \
echo "GRANT ALL PRIVILEGES ON *.* TO 'iu'@'localhost' WITH GRANT OPTION;" >> dbStart.dump && \
/etc/init.d/mysql start && mysql < dbStart.dump

# Connect CakePHP to Database
RUN sed -i 's/my_app/iu/g' /var/www/html/lamorisse/config/app.php && \
sed -i 's/secret/iu/g' /var/www/html/lamorisse/config/app.php

# Load our schema and Bootstrap CakePHP code
ADD project/db.sql db.sql
RUN /etc/init.d/mysql start && mysql -u iu -piu < db.sql && \
/var/www/html/lamorisse/bin/cake bake all users && \
/var/www/html/lamorisse/bin/cake bake all companys && \
/var/www/html/lamorisse/bin/cake bake all industry && \
/var/www/html/lamorisse/bin/cake bake all type && \
/var/www/html/lamorisse/bin/cake bake all risks && \
/var/www/html/lamorisse/bin/cake bake all requisites

# Expose ports
EXPOSE 80
EXPOSE 8765
EXPOSE 22

# Poor man's supervisor
CMD /etc/init.d/ssh start && \
/etc/init.d/apache2 start && \
/etc/init.d/mysql start && \
/var/www/html/lamorisse/bin/cake server -H 0.0.0.0 && \
tail -f /dev/null
