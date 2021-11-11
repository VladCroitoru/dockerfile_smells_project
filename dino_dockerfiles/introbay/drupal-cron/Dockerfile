FROM introbay/php:7.0-apache
MAINTAINER ignacio@introbay.com

RUN apt-get update && apt-get install -y cron && \
    rm -r /var/lib/apt/lists/*

# Install drush by using composer
ENV COMPOSER_HOME /root/composer
ENV COMPOSER_VERSION master

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
	&& composer global require drush/drush:8.* \
	&& ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/local/bin/drush \
	&& drush cache-clear drush

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/drush-cron
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/drush-cron
 
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
ENTRYPOINT []
CMD cron && tail -f /var/log/cron.log
