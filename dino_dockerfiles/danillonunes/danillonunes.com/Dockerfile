FROM alpine
MAINTAINER Danillo Nunes <marcus@danillo.net>

# Install dependencies
RUN apk add --update \
      curl \
      git \
      php-ctype \
      php-json \
      php-phar \
    && \

    curl http://files.drush.org/drush.phar -o drush.phar && \
    chmod +x drush.phar && \
    mv drush.phar /bin/drush && \
    drush init -y && \

    rm -rf /var/cache/apk/*

# Set work directory
WORKDIR "/danillonunes"

# Build Drupal site
COPY ["danillonunes.make", "./"]
RUN drush make danillonunes.make drupal

# Copy http directory and expose volumes
COPY ["http", "http"]
VOLUME ["/danillonunes", "/danillonunes/files/public", "/danillonunes/files/private"]

# Setup entrypoint
COPY ["docker/entrypoint.sh", ".docker/"]
ENTRYPOINT [".docker/entrypoint.sh"]
