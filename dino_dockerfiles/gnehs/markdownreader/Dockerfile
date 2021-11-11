FROM node:10-alpine
# Create app directory
WORKDIR /app
# Bundle app source
COPY . /app

RUN apk add --no-cache make gcc g++ python && \
    npm install --production && \
    npm cache clean --force && \
    apk del make gcc g++ python

ENV NODE_ENV=production
EXPOSE 3014
CMD ["npm", "start"]