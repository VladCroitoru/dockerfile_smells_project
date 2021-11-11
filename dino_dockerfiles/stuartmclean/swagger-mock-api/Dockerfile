From node:7-alpine

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Install app dependencies
COPY package.json /app/
RUN npm install --production

# Bundle app source
COPY . /app

EXPOSE 8080

CMD ["node", "server.js"]
