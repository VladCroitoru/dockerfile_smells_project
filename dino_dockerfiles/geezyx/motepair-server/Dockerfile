FROM node:5.9.1

# Create app directory
RUN mkdir -p /usr/src/motepair-server
WORKDIR /usr/src/motepair-server

# Install app dependencies
COPY package.json /usr/src/motepair-server/
RUN npm install

# Bundle app source
COPY . /usr/src/motepair-server

# Start server
CMD [ "node", "start.js" ]
