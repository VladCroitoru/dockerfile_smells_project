FROM node:argon

# Create app directory
RUN mkdir -p /usr/src/
WORKDIR /usr/src

# Install app dependencies
COPY package.json /usr/src/
RUN npm install

# Bundle app source
COPY . /usr/src/

EXPOSE 8080
CMD [ "npm", "start" ]


