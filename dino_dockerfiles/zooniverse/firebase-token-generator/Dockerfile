FROM node:7

# Install app dependencies
RUN mkdir /express-app
WORKDIR /express-app
COPY package.json /express-app/
RUN npm install

# Bundle app source
COPY . /express-app

# Run app
EXPOSE 8080
CMD ["node", "app.js"]
