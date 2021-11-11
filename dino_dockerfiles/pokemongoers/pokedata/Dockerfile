FROM node:4.0

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install -g grunt-cli
RUN npm install
# Bundle app source
COPY . /usr/src/app

RUN grunt apidoc

EXPOSE 8080

CMD [ "npm", "start" ]