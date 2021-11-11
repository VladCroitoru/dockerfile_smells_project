# Node 8
FROM node:8

# Create app directory
WORKDIR /usr/src/prices-tv-static

# Node configs
COPY package*.json ./
RUN npm install

# Bundle app source code (git?)
COPY . .

# Open port
EXPOSE 3000

# Start app
CMD [ "npm", "start" ]
