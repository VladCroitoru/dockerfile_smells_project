FROM node:14

# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /app
COPY server.js /app
COPY /app/dist /app/dist

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source


EXPOSE 5000
CMD [ "node", "server.js" ]