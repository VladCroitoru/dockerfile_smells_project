FROM node:10.16.0-alpine

#### Begin setup ####

# Installs docker
RUN apk add --update --no-cache bash bash-doc bash-completion

# Extra tools for native dependencies
RUN apk add --no-cache make gcc g++ python

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Env variables
ENV SERVER_PORT 3000

# Expose 3000
EXPOSE 3000

# Startup
ENTRYPOINT npm start
