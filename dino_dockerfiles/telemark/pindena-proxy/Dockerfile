###########################################################
#
# Dockerfile for pindena-proxy
#
###########################################################

# Setting the base to nodejs 4.2
FROM node:4.2

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install

# Env variables
ENV SERVER_PORT 8000
ENV PINDENA_URL https://telemark.pameldingssystem.no
ENV PINDENA_HOST: telemark.pameldingssystem.no
ENV PINDENA_PROTOCOL https
ENV PINDENA_PORT 443
ENV API_KEY yourSendGridAPIKey
ENV MAIL_TO mailTo@example.com

# Expose 8000
EXPOSE 8000

# Startup
ENTRYPOINT node standalone.js