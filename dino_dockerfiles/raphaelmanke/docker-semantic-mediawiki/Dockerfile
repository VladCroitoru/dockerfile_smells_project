ARG tag
FROM mediawiki:${tag:-1.30}
MAINTAINER Raphael Manke, Patrick Eisele

ENV COMPOSER_ALLOW_SUPERUSER = 1

RUN apt-get update && apt-get install -y \
		nano \
		wget \
		jq \
		unzip \
		libpng-dev

# install needed php extension
RUN docker-php-ext-install gd

# Copy scripts
COPY scripts ./scripts/check_db.sh ./
# Run the composer installation
RUN sh "install_composer.sh"

# Install semantic mediawiki
RUN php composer.phar require mediawiki/semantic-media-wiki "~2.5" --update-no-dev

# At containerstart run check script and then http server
CMD /var/www/html/check_db.sh && apache2-foreground
