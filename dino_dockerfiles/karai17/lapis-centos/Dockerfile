FROM openresty/openresty:centos

LABEL maintainer="Landon Manning <lmanning17@gmail.com>"

# Environment
ENV SERVER_MODE="production"
ARG OPENSSL_DIR="/usr/local/openresty/openssl"

# Prepare volumes
VOLUME /var/data
VOLUME /var/www

# Install from Yum
RUN yum -y install \
	gcc \
	openresty-openssl-devel \
	openssl-devel \
	unzip \
	; yum clean all

# Install from LuaRocks
RUN luarocks install luasec \
	&& luarocks install bcrypt \
	&& luarocks install busted \
	&& luarocks install i18n \
	&& luarocks install lapis \
		CRYPTO_DIR=${OPENSSL_DIR} \
		CRYPTO_INCDIR=${OPENSSL_DIR}/include \
		OPENSSL_DIR=${OPENSSL_DIR} \
		OPENSSL_INCDIR=${OPENSSL_DIR}/include \
	&& luarocks install luacov \
	&& luarocks install mailgun \
	&& luarocks install markdown

# Entrypoint
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Standard web port (use a reverse proxy for SSL)
EXPOSE 80

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
