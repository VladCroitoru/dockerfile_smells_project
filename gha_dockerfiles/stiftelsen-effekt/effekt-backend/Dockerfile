FROM node:14-alpine

#Setup folders
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app

#Install node packages
COPY package*.json ./
RUN npm install

#Copies source
COPY . .
COPY --chown=node:node . .

USER node

EXPOSE 8080

#Set environment varibales


#Setup default command to run server
CMD [ "node", "server.js" ]
