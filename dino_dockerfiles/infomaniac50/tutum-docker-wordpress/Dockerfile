FROM tutum/lamp:latest
MAINTAINER Fernando Mayo <fernando@tutum.co>, Feng Honglin <hfeng@tutum.co>

# Install plugins
RUN apt-get update && \
  apt-get -y install php5-gd curl && \
  rm -rf /var/lib/apt/lists/*

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN php wp-cli.phar --info --allow-root
RUN chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp

# Download latest version of Wordpress into /app
RUN rm -fr /app && wp --allow-root core download --path=/app/

# Configure Wordpress to connect to local DB
RUN wp --allow-root --path=/app/ core config --dbname=wordpress --dbuser=root --skip-check

# Modify permissions to allow plugin upload
RUN chown -R www-data:www-data /app/wp-content /var/www/html

# Add database setup script
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
ADD create_db.sh /create_db.sh
RUN chmod +x /*.sh


EXPOSE 80 3306
CMD ["/run.sh"]
