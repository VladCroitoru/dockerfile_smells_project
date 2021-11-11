FROM vergissberlin/debian-development

LABEL "de.andrelademann"="André Lademann" \
	version="0.0.1" \
	description="Docker debian image to use for php development, testing and deployment."

# Configure locales
ENV LANG en_US.UTF-8 \
		LANGUAGE en_US.UTF-8 \
		LC_ALL C.UTF-8 \
		LC_COLLATE C.UTF-8 \
		LC_CTYPE C.UTF-8 \
		LC_MONETARY C.UTF-8 \
		LC_MEASUREMENT C.UTF-8 \
		LC_MESSAGES C.UTF-8 \
		LC_NUMERIC C.UTF-8 \
		LC_PAPER C.UTF-8 \
		LC_RESPONSE C.UTF-8 \
		LC_TELEPHONE C.UTF-8 \
		LC_TIME C.UTF-8 \
		LC_TIME en_IE.UTF-8 \
		LC_PAPER en_IE.UTF-8 \
		LC_MEASUREMENT en_IE.UTF-8

# PHP packages
RUN apt-get update &&\
		apt-get install -y \
		php \
		php-apcu \
		php-cli \
		php-curl \
		php-dom \
		php-gd \
		php-intl \
		php-mbstring \
		php-pear \
		php-simplexml \
		php-soap \
		php-xdebug \
		php-zip

# PECL packages
RUN pecl install \
		xdebug

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# VPN configurations, keys, certificates
COPY setup/ /

# SSH port
EXPOSE 22

# Keep up, when stared
CMD ["/usr/sbin/sshd", "-D"]
