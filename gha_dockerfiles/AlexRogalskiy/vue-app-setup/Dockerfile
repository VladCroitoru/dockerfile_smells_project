FROM node:lts-alpine

# Working directory and mount volume
ARG PROJECT_DIR=/srv/app
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
VOLUME $PROJECT_DIR

# Install Vue CLI
RUN npm install -g @vue/cli

# Expose port to access web app
EXPOSE 8080
