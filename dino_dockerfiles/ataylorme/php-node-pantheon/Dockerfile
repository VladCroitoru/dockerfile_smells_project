# Start with PHP 7.1
FROM drupalci/php-7.1-apache:production

# Update
RUN apt-get update 

ENV \
	BACKSTOPJS_VERSION=3.0.25 \
	GULP_VERSION=3.9.1

# Install node/npm
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN \
	echo -e "\nInstalling nodejs..." && \
	apt-get install -y nodejs

# Install wget
RUN \
	echo -e "\nInstalling wget..." && \
	apt-get install -y wget

# Install rsync
RUN \
	echo -e "\nInstalling rsync..." && \
	apt-get install -y rsync

# Install ssh
RUN \
	echo -e "\nInstalling ssh..." && \
	apt-get install -y openssh-client

# Install gulp globally
RUN \
	echo -e "\nInstalling gulp v${GULP_VERSION}..." && \
	npm install -g gulp@${GULP_VERSION}

# Install Terminus
RUN \
	echo -e "\nInstalling Terminus 1.x..." && \
	/usr/bin/env COMPOSER_BIN_DIR=$HOME/bin composer --working-dir=$HOME require pantheon-systems/terminus "^1"

# Enable Composer parallel downloads
RUN \
	echo -e "\nInstalling hirak/prestissimo for parallel Composer downloads..." && \
	composer global require -n "hirak/prestissimo:^0.3"

# Install Terminus plugins
RUN \
	echo -e "\nInstalling Terminus plugins..." && \
	mkdir -p $HOME/.terminus/plugins && \
	composer create-project -n -d $HOME/.terminus/plugins pantheon-systems/terminus-build-tools-plugin:dev-master && \
	composer create-project -n -d $HOME/.terminus/plugins pantheon-systems/terminus-secrets-plugin:^1
