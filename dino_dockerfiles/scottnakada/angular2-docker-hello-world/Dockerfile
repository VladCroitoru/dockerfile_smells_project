# To build and run with Docker:
#
#  $ docker build -t angular2-quickstart .
#  $ docker run -it --rm -p 3000:3000 -p 3001:3001 -v $(pwd)/app:/quickstart/app angular2-quickstart
#
# Start with a default nodejs image
FROM node:latest

# Add some necessary packages
RUN apt-get update
RUN apt-get install -y vim

# Create a nodejs account, in nodejs group, with home directory /home/nodejs
RUN mkdir -p /quickstart/app /home/nodejs && \
    groupadd -r nodejs && \
    useradd -r -g nodejs -d /home/nodejs -s /sbin/nologin nodejs && \
    chown -R nodejs:nodejs /home/nodejs

# Use /quickstart as the working directory
WORKDIR /quickstart

# Add build files to /quickstart
ADD package.json typings.json tsconfig.json systemjs.config.js index.html styles.css /quickstart/
ADD app/* /quickstart/app/
RUN chown -R nodejs:nodejs /quickstart
# install npm packages as root; but allow nodejs user to install later
RUN npm install --unsafe-perm=true

# Startup as user nodejs
USER nodejs

EXPOSE 3000 3001

# Start the web-server
CMD npm start
