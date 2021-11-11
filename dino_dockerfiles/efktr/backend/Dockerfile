FROM node:boron

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

# Use defaults or ENV file
RUN npm install

EXPOSE 3300

CMD [ "npm", "start" ]