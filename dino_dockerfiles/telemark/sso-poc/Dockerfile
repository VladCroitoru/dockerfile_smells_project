# Setting the base to nodejs 10.0.0
FROM node:10.16.2-alpine@sha256:0d5abfc8ef9d0984010a05e234324e517620af096b8aeb2fabc841157ef2e676

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Env variables
ENV SERVER_PORT 8000

# Expose 3000
EXPOSE 8000

# Startup
ENTRYPOINT node standalone.js