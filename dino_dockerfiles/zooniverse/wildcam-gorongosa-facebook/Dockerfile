FROM node:argon

# Install app dependencies
RUN mkdir /app
WORKDIR /app
COPY package.json /app/
RUN npm install

# Bundle app source
COPY . /app

# Run app
EXPOSE 8080
RUN npm run build
CMD ["node", "docker-server.js"]
