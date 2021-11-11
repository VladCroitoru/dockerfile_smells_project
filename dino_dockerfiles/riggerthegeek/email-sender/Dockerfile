########################################
# Docker                               #
#                                      #
# A NodeJS container that enables the  #
# application to run                   #
########################################

FROM node:6.5

MAINTAINER Simon Emms, simon@simonemms.com

# Set the work directory and add the project files to it
WORKDIR /opt/email-sender
ADD . /opt/email-sender

# Environment variables
ENV COUNT_FLAG sendAttempts
ENV MONGODB_COLLECTION email
ENV MONGODB_URL mongodb://localhost
ENV NPM_CONFIG_LOGLEVEL warn
ENV RETRY 3
ENV SENT_FLAG sent
ENV TIMEOUT 30000

# Install the dependencies
RUN npm install

# Expose the port
EXPOSE 9999

# Run run run
CMD npm start