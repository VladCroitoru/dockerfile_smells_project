FROM node:6-slim

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

# Expose Faye on HTTP port
ENV FAYE_PORT 80
EXPOSE 80

# Start app
CMD [ "npm", "start" ]
