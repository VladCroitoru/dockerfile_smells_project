FROM node:6-wheezy@sha256:856079c8623dba2eb0a5fbbebb52a34d4057ad0d8b78c1d93b6377f7a251f6fb

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
#TODO: It's usually best to do this after the npm install so that the
#      npm install doesn't need happen everytime the src changes.
#      In this case I have steps in the postinstall that need these
#      files here... Should review
COPY . /usr/src/app

# Install app dependencies
#COPY package.json /usr/src/app/
RUN npm install

RUN npm run bower

# Bundle app source
#COPY . /usr/src/app

CMD [ "node", "app.js" ]
