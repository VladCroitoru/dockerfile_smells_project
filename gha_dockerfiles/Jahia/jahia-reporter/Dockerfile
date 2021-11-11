# Imported from: https://github.com/oclif/docker/blob/master/Dockerfile
FROM node:alpine

LABEL Jahia Dev Team

# Add bash
RUN apk add --no-cache bash

WORKDIR /usr/share/jahia-reporter/

RUN npm install -g @jahia/jahia-reporter@latest

CMD ["/bin/bash"]