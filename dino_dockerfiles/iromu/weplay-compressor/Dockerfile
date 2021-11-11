FROM node:6

# Create app directory
RUN mkdir -p /usr/src/app/compressor
WORKDIR /usr/src/app/compressor

COPY . .

# Install app dependencies
RUN npm install --production

# Setup environment
ENV NODE_ENV production
ENV WEPLAY_REDIS_URI "redis:6379"
ENV WEPLAY_LOGSTASH_URI "logstash:5001"

# Run
CMD ["node", "index.js"]