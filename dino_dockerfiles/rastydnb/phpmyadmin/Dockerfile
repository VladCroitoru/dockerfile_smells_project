FROM maxexcloo/nginx-php:latest
MAINTAINER Luis Ramos <momia191@gmail.com>
ENV VERSION 4.4.11
RUN mkdir -p /data/http && \
	cd /data/http && \
	wget -O - "https://files.phpmyadmin.net/phpMyAdmin/${VERSION}/phpMyAdmin-${VERSION}-all-languages.tar.gz" | tar --strip-components=1 -x -z && \
	rm -rf *.md .coveralls.yml ChangeLog composer.json config.sample.inc.php DCO doc examples phpunit.* README RELEASE-DATE-* setup
ADD data /data

WORKDIR /data/http/themes
RUN  wget "https://files.phpmyadmin.net/themes/metro/2.3/metro-2.3.zip"
RUN  unzip metro-2.3.zip
RUN  rm metro-2.3.zip
