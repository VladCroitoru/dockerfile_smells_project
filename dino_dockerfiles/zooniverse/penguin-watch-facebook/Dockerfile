FROM node:0.10

# Install app dependencies
RUN mkdir /app
WORKDIR /app
COPY package.json /app/
RUN npm install

# Bundle app source
COPY . /app

# Run app
EXPOSE 80
ENV FB_ENV production
RUN npm run build-facebook
CMD ["node", "docker-server.js"]
