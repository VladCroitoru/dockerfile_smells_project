# Setting the base to nodejs 8.2.1
FROM node:8.2.1-alpine

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Tries to fix installation of form-data
RUN npm install git+https://github.com/telemark/form-data.git

# Startup
ENTRYPOINT node example.js
