# Start with the latest node version and yarn installation
FROM node:latest

# Install latest Meteor
RUN curl https://install.meteor.com | sh

# Print yarn version for peace of mind
RUN yarn --version

# used to update settings files with generated urls
RUN yarn global add json
