FROM php:7.1-cli

# Configure the system
RUN apt-get update \
 && apt-get install -y --no-install-recommends --fix-missing \
    ca-certificates \
 	curl \
 	git \
	wget \
	zlib1g-dev

# Copy over the entry point and data which will be executed.
COPY .docker/entry-point.sh /usr/bin/entry-point
ADD . /usr/local/pktool

# Install a separate user and make sure this container is ran as the user.
RUN addgroup pktool \
 && adduser --no-create-home --disabled-password --ingroup pktool --gecos pktool pktool \
 && mkdir -p /data \
 && chown -R pktool:pktool /data \
 && chmod +x /usr/bin/entry-point

# Install the zip extension
RUN docker-php-ext-install zip \
 && docker-php-ext-enable zip

# Install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
 && php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
 && php composer-setup.php \
 && php -r "unlink('composer-setup.php');" \
 && mv composer.phar /usr/local/bin/composer \
 && composer self-update \
 && chown pktool:pktool /usr/local/bin/composer

# The directory to work from.
WORKDIR /usr/local/pktool

# Install Composer dependencies
RUN composer install --no-dev -o

# The volume that can be mounted
VOLUME /data

# The directory to work from.
WORKDIR /data

ENV GOSU_VERSION 1.10
RUN set -ex; \
	\
	fetchDeps=' \
		ca-certificates \
		wget \
	'; \
	apt-get update; \
	apt-get install -y --no-install-recommends $fetchDeps; \
	rm -rf /var/lib/apt/lists/*; \
	\
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"; \
	\
# verify the signature
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
	gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
	rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \
	\
	chmod +x /usr/local/bin/gosu; \
# verify that the binary works
	gosu nobody true;

# The file to run
ENTRYPOINT ["/usr/bin/entry-point", "/usr/local/pktool/bin/pktool"]
