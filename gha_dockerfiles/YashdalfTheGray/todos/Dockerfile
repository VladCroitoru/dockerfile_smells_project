FROM node

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json package-lock.json /usr/src/app/
RUN apk add --no-cache --virtual .gyp python make g++
RUN npm install

# Bundle app source
COPY . /usr/src/app
RUN npm run tslint

EXPOSE 8080

CMD [ "npm", "start" ]
