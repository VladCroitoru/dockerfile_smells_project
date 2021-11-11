# Dockerfile Joomla with Multibyte String
# acdaic4v 05.04.2016

FROM joomla:3.6.5
MAINTAINER acdaic4v <acdaic4v@sloervi.de>

# Rename original config file
RUN /bin/mv /etc/apache2/mods-available/php5.load /etc/apache2/mods-available/php5.load.or

# Install the module and give me a vi
RUN apt-get update && apt-get install -y libapache2-mod-php5 vim php5-mysql

# Enable mbstring to use UTF-8
RUN docker-php-ext-install mbstring
