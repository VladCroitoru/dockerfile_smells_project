FROM node:argon

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install the app
COPY package.json /usr/src/app
RUN npm install
COPY . /usr/src/app

EXPOSE 4333
CMD [ "npm", "start" ]
