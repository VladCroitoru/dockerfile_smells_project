FROM node:boron

MAINTAINER didstopia

# Fixes apt-get warnings
ENV DEBIAN_FRONTEND noninteractive

# Run a quick apt-get update/upgrade
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get autoremove -y

# Install dependencies
RUN apt-get install -y \
	ca-certificates \
    software-properties-common \
    python-software-properties \
    curl \
    bsdtar \
    jq

# Create app directory
RUN mkdir -p /usr/src/app

# Download and extract the app
RUN curl -sL https://github.com/Dids/albion-discordbot/archive/bdefea03029db1654a1f98d43854aa933eee272f.zip | bsdtar -xvf- -C /tmp && \
	mv /tmp/albion-discordbot-bdefea03029db1654a1f98d43854aa933eee272f/* /usr/src/app/ && \
	rm -fr /tmp/albion-discordbot-bdefea03029db1654a1f98d43854aa933eee272f

# Install app dependencies
WORKDIR /usr/src/app
RUN npm install
WORKDIR /

# Copy scripts
COPY bootstrap.sh /start.sh

# Fix permissions
RUN chmod +x /start.sh

# Run the app with our custom bootstrapper
ENTRYPOINT ["/start.sh"]
