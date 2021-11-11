FROM node:alpine

# Create volume to persist sqlite database
VOLUME /usr/src/app/local-db

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install --only=production
# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY . .

EXPOSE 3000

ENV NODE_ENV production

CMD [ "node", "index.js" ]

