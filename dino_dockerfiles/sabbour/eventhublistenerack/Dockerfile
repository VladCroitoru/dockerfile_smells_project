FROM node:boron

# Create app directory
RUN mkdir -p /usr/src/eventlistener
WORKDIR /usr/src/eventlistener

# EH
ENV EVENTHUBCONNSTRING=
ENV EVENTHUBPATH=

# ACK Logging
ENV TEAMNAME=

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

# Install app dependencies
RUN npm install

# Bundle app source
COPY . .

CMD [ "node", "eventlistener.js" ]