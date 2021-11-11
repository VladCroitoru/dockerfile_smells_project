###########################################################
#
# Dockerfile for tfk-seneca-mail
#
###########################################################

# Setting the base to nodejs 4.6.0
FROM mhart/alpine-node:4.6.0

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
ENV TFK_SENECA_MAIL_TAG tfk-seneca-mail
ENV TFK_SENECA_MAIL_HOST localhost
ENV TFK_SENECA_MAIL_PORT 8000
ENV TFK_SENECA_MAIL_SENDGRID_API_KEY your-sendgrid-api-key

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]