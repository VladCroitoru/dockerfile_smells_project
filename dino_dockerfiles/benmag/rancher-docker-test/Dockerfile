FROM richarvey/nginx-php-fpm

# Build commands 
# This is probably better done 
# as an ARG but I don't know 
# if Rancher supports that 
ENV BUILD_COMMANDS \
	cd /app && \
	composer create-project && \
	composer install --no-interaction
	# add the migration to the build commands in the MasonJson
	# php artisan migrate 

# Install some dependencies
RUN apt-get update && \
	apt-get install curl nano && \
	curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add updated nginx config
COPY conf/nginx-site.conf /etc/nginx/sites-available/default.conf

# Add environment variable config
COPY conf/env.conf /etc/nginx

# Bundle app source
COPY app/ /app

# Install app dependencies
RUN cd /app && \
	composer create-project && \
	composer install --no-interaction 
	
# Set required permissions
RUN chmod -R 777 /app/storage && \
	chmod -R 777 /app/storage/logs && \
	chmod -R 777 /app/bootstrap/cache

# Add script that adds env vars into config file for nginx
COPY files/copyenv /
RUN chmod 755 /copyenv

# Add run script
COPY files/run.sh /
RUN chmod 755 /run.sh

# Expose ports 
EXPOSE 80

# Start 
CMD ["/bin/bash", "/run.sh"]
