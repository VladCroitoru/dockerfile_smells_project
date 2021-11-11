FROM node:14.17-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json .npmrc /usr/src/app/
RUN npm ci && rm -f .npmrc

# Bundle app source
COPY . /usr/src/app

ENV PORT=80 NODE_ENV=production

EXPOSE 80

CMD [ "node" , "./bin/start"]
