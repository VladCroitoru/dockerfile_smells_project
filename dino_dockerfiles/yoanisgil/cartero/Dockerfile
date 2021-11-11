FROM node:0.12-slim

# Application will be launched from /srv/www, so make sure it exists.
RUN mkdir -p /srv/www

# Add source files & deps
ADD . /srv/www

# Since application will be launched from /srv/www it's very convenient to set it up as the working directory
WORKDIR /srv/www

# Exclude npm cache from the image
VOLUME /root/.npm

# By default we install dependencies.
RUN npm install
