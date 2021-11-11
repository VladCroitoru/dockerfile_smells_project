FROM httpd:alpine

# Default username, password and UID.
ENV AUTH_USER username
ENV AUTH_PASS password

# Enable vhosts.
RUN sed -i -e 's%#Include conf/extra/httpd-vhosts.conf%Include conf/extra/httpd-vhosts.conf%g' /usr/local/apache2/conf/httpd.conf

# Add our custom vhost.
COPY vhost.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf

# Create server root and set it as workdir.
WORKDIR /var/www

# Add entrypoint to create .htpasswd file.
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 80

CMD ["httpd-foreground"]