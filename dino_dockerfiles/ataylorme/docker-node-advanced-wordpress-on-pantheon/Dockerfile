FROM node:8.11.2

# Set environment variables
ENV \
	JEST_VERSION=23.1.0 \
	GULP_VERSION=4.0.0 \
	GULP_CLI_VERSION=2.0.1 \
	GRUNT_VERSION=1.0.1 \
	WEBPACK_VERSION=3.8.1 \
	BACKSTOP_CRAWL_VERSION=2.3.1 \
	PHANTOMJS_VERSION=2.1.7 \
	CASPERJS_VERSION=1.1.4 \
	SLIMERJS_VERSION=0.10.3 \
	BACKSTOPJS_VERSION=latest \
	# Workaround to fix phantomjs-prebuilt installation errors
	# See https://github.com/Medium/phantomjs/issues/707
	NPM_CONFIG_UNSAFE_PERM=true

# Run updates
RUN \
	echo -e "\nRunning apt-get update..." && \
	apt-get update

# Base packages
RUN \
	echo -e "\nInstalling base packages..." && \
	apt-get install -y git sudo software-properties-common python-software-properties libx11-xcb1

# Upgrade NPM
RUN \
	echo -e "\nUpgrading NPM to the latest..." && \
	npm install -g npm@latest

RUN echo -e "\nInstalling BackstopJS Node modules..."
RUN sudo npm install -g --unsafe-perm=true --allow-root phantomjs@${PHANTOMJS_VERSION}
RUN sudo npm install -g --unsafe-perm=true --allow-root casperjs@${CASPERJS_VERSION}
RUN sudo npm install -g --unsafe-perm=true --allow-root slimerjs@${SLIMERJS_VERSION}
RUN sudo npm install -g --unsafe-perm=true --allow-root backstopjs@${BACKSTOPJS_VERSION}

RUN echo -e "\nInstalling Google Chrome..."
RUN wget https://dl-ssl.google.com/linux/linux_signing_key.pub && sudo apt-key add linux_signing_key.pub
RUN sudo add-apt-repository "deb http://dl.google.com/linux/chrome/deb/ stable main"

RUN	apt-get -y update && \
	apt-get -y install google-chrome-stable

RUN apt-get install -y firefox-esr

# Install jq
RUN \
	echo -e "\nInstalling jq..." && \
	apt-get -y install jq

# Install wget
RUN \
	echo -e "\nInstalling wget..." && \
	apt-get -y install wget


# Install openssl
RUN \
	echo -e "\nInstalling openssl..." && \
	apt-get -y install openssl

# Install git
RUN \
	echo -e "\nInstalling git..." && \
	apt-get -y install git

# Install ssh
RUN \
	echo -e "\nInstalling ssh..." && \
	apt-get -y install ssh

# Install rsync
RUN \
	echo -e "\nInstalling rsync..." && \
	apt-get -y install rsync

# Install gulp globally
RUN \
	echo -e "\nInstalling gulp $GULP_VERSION..." && \
	npm install -g gulp@${GULP_VERSION}

# Install gulp-cli globally
RUN \
	echo -e "\nInstalling gulp-cli $GULP_CLI_VERSION..." && \
	npm install -g gulp-cli@${GULP_CLI_VERSION}

# Install grunt globally
RUN \
	echo -e "\nInstalling grunt $GRUNT_VERSION..." && \
	npm install -g grunt@${GRUNT_VERSION}

# Install backstop-crawl globally
RUN \
	echo -e "\nInstalling backstop-crawl $BACKSTOP_CRAWL_VERSION..." && \
	npm install -g backstop-crawl@${BACKSTOP_CRAWL_VERSION}

# Install webpack globally
RUN \
	echo -e "\nInstalling webpack $WEBPACK_VERSION..." && \
	npm install -g webpack@${WEBPACK_VERSION}

# Install jest globally
RUN \
	echo -e "\nInstalling jest $JEST_VERSION..." && \
	npm install -g jest@${JEST_VERSION}
