FROM node:14

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm ci --only=production

# Bundle app source
COPY . .

# server port is open on 8080, so docker needs to expose it's virtual machine port
EXPOSE 8080
# start the app here
CMD [ "node", "index.js" ]