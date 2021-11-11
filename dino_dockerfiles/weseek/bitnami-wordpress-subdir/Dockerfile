FROM bitnami/wordpress:4.8.3-r0

# Add new scripts and configs to use sub directory.
COPY ./scripts/app-entrypoint.sh /app-entrypoint.sh

# Remove config file original to replace.
RUN mkdir /configs
COPY ./configs/wordpress-vhost.conf /configs
COPY ./configs/wordpress-https-vhost.conf /configs

