FROM mhart/alpine-node:10

#### Begin setup ####

# Installs git
RUN apk add --update git && rm -rf /var/cache/apk/*

# Bundle app source
COPY . /src

# Change working directory
WORKDIR /src

# Install dependencies
RUN npm install --production

# Startup
ENTRYPOINT node example.js