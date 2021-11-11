FROM node:6.9

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle the needed source files
COPY package.json /usr/src/app
COPY gulpfile.js /usr/src/app/gulpfile.js
COPY src /usr/src/app/src

# Copy the default config to config.js
RUN mkdir /usr/src/app/config
COPY config/config.default.js /usr/src/app/config/config.js

# Download and unpack Maxmind GeoLite2 Lite library
RUN mkdir data
WORKDIR /usr/src/app/data
RUN curl -O http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz && gunzip GeoLite2-City.mmdb.gz
WORKDIR /usr/src/app

# Install packages
RUN npm install --loglevel warn

# Build
RUN npm run production

# Start application as default action
EXPOSE 8080
ENTRYPOINT [ "npm", "start", "--" ]