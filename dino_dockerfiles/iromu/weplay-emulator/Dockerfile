FROM node:7

# Create app directory
RUN mkdir -p /usr/src/app/emulator
WORKDIR /usr/src/app/emulator

COPY . .

# Install build dependencies
RUN apt-get update
RUN apt-get install -y libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install app dependencies
RUN npm install

# Setup environment
ENV NODE_ENV production
ENV WEPLAY_REDIS_URI "redis:6379"
ENV WEPLAY_LOGSTASH_URI "logstash:5001"

# Run
CMD [ "node", "index.js" ]