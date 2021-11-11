FROM centurylink/apache-php
MAINTAINER inhumantsar

### Fetch updates
RUN apt-get update && \
		DEBIAN_FRONTEND=noninteractive apt-get -y upgrade

### Download Joomla into /var/www/html
WORKDIR /app
RUN rm -rf /app/* && \
		git clone -b master https://github.com/joomla/joomla-cms.git .

#### Config perms
RUN chown -R www-data:www-data /var/www/html
