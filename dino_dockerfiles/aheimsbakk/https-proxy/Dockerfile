#
# If you don't specify any certs folder a selfsigned certificate will be used.
# Only use the selfsigned certificate for testing.
#

# Use oldee stable
FROM aheimsbakk/base-debian:latest

# Yep thats me, please use +docker tag to help me find the mail
MAINTAINER Arnulf Heimsakk "arnulf.heimsbakk+docker@gmail.com"

# Will only allow one HTTP port if defined
# Redirects to first PORT_HTTPS
ENV PORT_HTTP 80

# Apache ports, more than one port mapping can be specified with space
ENV PORT_HTTPS 443
ENV PORT_REDIRECT 80

# Change to your servers FQDN
ENV SERVER_NAME localhost

# Change to your webmaster email
ENV SERVER_ADMIN webmaster@$SERVER_NAME

# Strict transport age
ENV SSL_STRICT_TRANSPORT max-age=31536000; includeSubDomains

# Server SSL chiphers to use
ENV SSL_CIPHERS EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH

# SSL cert file
ENV SSL_CERT_FILE /etc/ssl/private/cert.pem
ENV SSL_PRIVKEY_FILE /etc/ssl/private/privkey.pem
ENV SSL_CHAIN_FILE /etc/ssl/private/chain.pem

# Additional ProxyPass parameters
ENV PROXYPASS_CONFIG retry=60

# Install apache2 and haveged for entropy
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 openssl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure apache servername
RUN echo ServerName \${SERVER_NAME} > /etc/apache2/conf-available/servername.conf
RUN a2enconf servername

# Add ssl, rewrite, headers and proxy module
RUN a2enmod ssl rewrite headers proxy_http

# Remove default site
RUN a2dissite 000-default

# Add redirect from port 80 to ssl, and the ssl site
ADD site-redirect.conf      /etc/apache2/sites-available/redirect.conf
ADD site-ssl.conf           /etc/apache2/sites-available/ssl.conf

# Generate a a selfsigned certificate just for testing using $SERVER_NAME
# as server name; valid for 365 after build of docker
RUN test -f "$SSL_PRIVKEY_FILE" || echo -n NO\\n.\\n.\\n.\\nWaffle Company Inc\\nBranding\\n$SERVER_NAME\\n$SERVER_ADMIN\\n | openssl req -x509 -newkey rsa:4096 -sha256 -keyout "$SSL_PRIVKEY_FILE" -out "$SSL_CERT_FILE" -days 365 -nodes && ln -s "$SSL_CERT_FILE" "$SSL_CHAIN_FILE"

# Expose certificate directory
VOLUME /etc/ssl/private

# Expose
EXPOSE 80 443

# Add entrypoint
COPY docker-entrypoint.sh /

# Entrypoint that generates APACHE site configuration for each LISTEN address mapping
ENTRYPOINT ["/docker-entrypoint.sh"]

# Run apache
CMD ["apache2ctl", "-DFOREGROUND"]

