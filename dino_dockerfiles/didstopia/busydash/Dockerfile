# Use the smallest mini-image available for NodeJS
FROM metocean/mini-nodejs

MAINTAINER Didstopia <support@didstopia.com>

# Install updates and dependencies
RUN apk update && \
	apk upgrade && \
	apk add --no-cache \
	bash \
	unzip \
	curl \
	perl

# Download and extract linux dash
RUN curl -k -L -o master.zip https://github.com/afaqurk/linux-dash/archive/master.zip && \
	unzip master.zip && \
	mv linux-dash-master / && \
	rm -f master.zip

# Configure linux dash
WORKDIR linux-dash-master
RUN npm install

# Remove apk caches (just in case)
RUN rm -rf /var/cache/apk/*

# Expose any ports
EXPOSE 80

# Start the server
ENTRYPOINT ["node", "server"]
