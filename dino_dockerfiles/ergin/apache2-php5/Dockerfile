FROM tutum/apache-php
MAINTAINER Ergin BULUT <ergin@erginbulut.com>

# Install neccessary apps and php extensions.
RUN apt-get update \
	&& apt-get -yq install \
	wget \
	git-core \
	php5-memcache \
	php5-json \
    && apt-get -y upgrade \
    && apt-get clean \
    && apt-get autoclean \
    && apt-get autoremove

# Enable neccessary Apache modules.
RUN a2enmod expires deflate headers rewrite

# Enable neccessary existing extensions and increase upload size
RUN sed -i.bak 's/upload_max_filesize = 2M/upload_max_filesize = 16M/g' /etc/php5/apache2/php.ini && \
    sed -i.bak 's/post_max_size = 8M/post_max_size = 16M/g' /etc/php5/apache2/php.ini
