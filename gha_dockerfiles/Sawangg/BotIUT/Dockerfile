FROM node:16.10-alpine

# Install python
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

# Install build-make
RUN apk add build-base --no-cache

# Install git
RUN apk add git --no-cache

# Install the bot
WORKDIR /home/node/app
COPY package.json ./
RUN npm install
COPY . /home/node/app

# Run the app
RUN npm run build
CMD [ "npm", "start" ]