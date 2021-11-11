###########################################################
#
# Dockerfile for tfk-saksbehandling-fara-import
#
###########################################################

# Setting the base to nodejs 4.4.7
FROM mhart/alpine-node:4.4.7

# Maintainer
MAINTAINER Jonas Enge

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
ENV TFK_SFI_JWT_KEY Louie Louie, oh no, I got to go. Louie Louie, oh no, I got to go
ENV TFK_SFI_CALLBACK_STATUS_MESSAGE Søknad importert
ENV TFK_SFI_JOB_DIRECTORY_PATH test/data/fara
ENV TFK_SFI_DISTRIBUTION_DIRECTORY_PATH test/data/distribution
ENV TFK_SFI_ARCHIVE_DIRECTORY_PATH test/data/archive
ENV TFK_SFI_DONE_DIRECTORY_PATH test/data/fara/done
ENV TFK_SFI_ERROR_DIRECTORY_PATH test/data/errors
ENV TFK_SFI_API_URL https://api.skoleskyss.t-fk.no/applications

# Startup
ENTRYPOINT node example.js
