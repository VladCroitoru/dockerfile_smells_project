FROM node:7

# Create app directory
RUN mkdir -p /usr/src/app/io
WORKDIR /usr/src/app/io

COPY . .

# Install app dependencies
RUN npm install

# Setup environment
ENV NODE_ENV production
ENV WEPLAY_PORT 8081
ENV WEPLAY_REDIS_URI "redis:6379"
ENV WEPLAY_REDIS "redis://redis:6379"
ENV WEPLAY_LOGSTASH_URI "logstash:5001"

EXPOSE 8081

# Run
CMD [ "node", "index.js" ]