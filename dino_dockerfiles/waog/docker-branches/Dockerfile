FROM node:6

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

# install dependencies
RUN npm install

EXPOSE 3000
CMD [ "node", "index.js" ]