# Setting the base to nodejs 4.8.7
FROM node:4.8.7-alpine

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Extra tools for native dependencies
RUN apk add --no-cache make gcc g++ python

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

EXPOSE 8000

# Startup
CMD ["node", "server.js"]
