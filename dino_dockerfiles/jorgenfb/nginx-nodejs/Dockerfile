#
# Nginx with nodejs and npm Dockerfile
#
# https://github.com/jorgenfb/nginx-nodejs
#

# Pull base image.
FROM dockerfile/nginx

# Install Node.js
RUN \
  apt-get update && \
  apt-get install -y curl && \
  curl -sL https://deb.nodesource.com/setup | bash - && \
  apt-get install -y nodejs && \
  apt-get purge -y curl apt-transport-https && \
  apt-get autoremove -y && \
  apt-get clean all
