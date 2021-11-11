###########################################################
#
# Dockerfile for portalen-roles
#
###########################################################

# Setting the base to nodejs 4.6.2
FROM mhart/alpine-node:4.6.2

# Maintainer
MAINTAINER Geir Gåsodden

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

# Env variables
ENV PORTALEN_ROLES_TAG portalen-roles
ENV PORTALEN_ROLES_URL http://roles.portalen.no
ENV PORTALEN_ROLES_HOST localhost
ENV PORTALEN_ROLES_PORT 8000

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]