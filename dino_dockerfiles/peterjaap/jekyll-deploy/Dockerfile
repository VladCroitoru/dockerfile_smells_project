FROM srcoder/development-php:php71-fpm
MAINTAINER Peter Jaap Blaakmeer <peterjaap@elgentos.nl>

RUN apt-get update --fix-missing && apt-get install -y \
	git-core \
	curl \
	zlib1g-dev \
	build-essential \
	libssl-dev \
	libreadline-dev \
	libyaml-dev \
	libsqlite3-dev \
	sqlite3 \
	libxml2-dev \
	libxslt1-dev \
	libcurl4-openssl-dev \
	python-software-properties \
	libffi-dev \
	nodejs \
	ruby-full

RUN gem install bundler

RUN curl -LO https://deployer.org/deployer.phar && mv deployer.phar /usr/local/bin/dep && chmod +x /usr/local/bin/dep

