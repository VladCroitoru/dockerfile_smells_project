# Setting the base to nodejs 8.9.4
FROM node:8.9.4-alpine

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Expose 8080
EXPOSE 8080

# Startup
ENTRYPOINT npm start