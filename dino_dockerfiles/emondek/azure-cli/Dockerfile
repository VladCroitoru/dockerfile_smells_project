# Create the AzureCLI image
FROM ubuntu:14.04
MAINTAINER Ed Mondek <emondek@hotmail.com>
RUN apt-get update && apt-get install -y \
  nodejs-legacy \
  npm
RUN npm install -g azure-cli

