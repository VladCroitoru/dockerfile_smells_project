FROM node:4.6.1-slim
MAINTAINER Scott Linton <talltechdude@gmail.com>

# Install app
ADD package.json /app/package.json
WORKDIR /app
RUN npm install --silent --production
ADD . /app

# Set environment
ENV PORT 8000
EXPOSE 8000

VOLUME /opt/factorio/saves
VOLUME /opt/factorio/mods
VOLUME /opt/factorio/data

CMD node /app
