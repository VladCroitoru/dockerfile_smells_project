FROM ubuntu:trusty
MAINTAINER Wilson Santos <wilson@xyber.ph>

# Present dpkg errors
ENV TERM=xterm-256color

# set mirrors to ris.ph/ubuntu
RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirror.rise.ph\/ubuntu/g" /etc/apt/sources.list

# Install node.js
RUN apt-get update && \
    apt-get install curl -y && \
    curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \
    apt-get install -y nodejs

COPY . /app
WORKDIR /app

# Install application dependencies
RUN npm install -g mocha && \
    npm install

# Add mocha test runner as entrypoint
ENTRYPOINT ["mocha"]

