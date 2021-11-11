FROM		ubuntu:14.04
MAINTAINER	technopreneural@yahoo.com

# Enable (or disable) apt-cache proxy
#ENV		http_proxy http://acng.robin.dev:3142

# Install packages
RUN			apt-get update \
			&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
				debconf-utils \
				openssl \
				apache2 \
				apache2-utils \

# Delete downloaded data afterwards to reduce image footprint
			&& rm -rf /var/lib/apt/lists/* \

# Fix warnings
			&& echo "ServerName localhost" >> /etc/apache2/conf-available/servername.conf && a2enconf servername \

# Create self-signed SSL certificate
			&& mkdir /etc/apache2/ssl \
			&& openssl req \
				-x509 \
				-nodes \
				-days 365 \
				-newkey rsa:2048 \
				-keyout /etc/apache2/ssl/apache2.key \ 
				-out /etc/apache2/ssl/apache2.crt \
				-subj "/CN=docker-ubuntu-14.04-apache2" \

# Remove packages to reduce image size
#			&& apt-get purge openssl \
#			&& apt-get autoremove --purge \

# Install SSL certificate
			&& sed -i -e "s|/etc/ssl/certs/ssl-cert-snakeoil.pem|/etc/apache2/ssl/apache2.crt|g" /etc/apache2/sites-available/default-ssl.conf \
			&& sed -i -e "s|/etc/ssl/private/ssl-cert-snakeoil.key|/etc/apache2/ssl/apache2.key|g" /etc/apache2/sites-available/default-ssl.conf \

# Enable SSL
			&& a2enmod ssl \

# Enable mod_rewrite
			&& a2enmod rewrite \
			&& sed -i -e '/^<Directory \/var\/www\/>/,/^<\/Directory>/s/\(AllowOverride \)None/\1All/' /etc/apache2/apache2.conf \

# Disable default site(s)
			&& a2dissite 000-default \
			&& a2dissite default-ssl 

COPY		./apache2-entrypoint.sh /

ENTRYPOINT	["/apache2-entrypoint.sh"]

# Create volume for host folder
# NOTE: use "docker run -v <folder_path>:<volume>..." to bind volume to host folder
VOLUME		["/var/www/html", "/var/log/apache2"]]

# Expose port 80 and 443 (HTTP and HTTPS/SSL) to other containers
# NOTE: use "docker run -p 80:80 -p 443:443..." to map exposed port(s) to host ports
EXPOSE		80 443 
