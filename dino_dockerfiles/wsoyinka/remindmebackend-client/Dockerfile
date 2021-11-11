FROM ubuntu:xenial
MAINTAINER wale soyinka <wsoyinka@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# RUN sed -i "s/http:\/\/archive./http:\/\/ca.archive./g" /etc/apt/sources.list 

# Install node.js
RUN apt-get update && \
    apt-get install -y  sudo curl git apt-transport-https ca-certificates && \
    curl --fail -ssL -o setup-nodejs https://deb.nodesource.com/setup_6.x && \
    sudo bash setup-nodejs && \
    apt-get update && \
    apt-get install -y nodejs 

ADD . /app
WORKDIR /app

# Install application dependencies
RUN npm install -g grunt-cli && \
    npm install --unsafe-perm=true

# Set entrypoint
CMD ["node","app.js"]
