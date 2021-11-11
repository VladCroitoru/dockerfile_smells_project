#prod
FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

ENV NODE_ENV=production

EXPOSE 4000

CMD [ "node", "dist/index.js" ]
USER node

# #dev.
# #This needs to be updated to replace nodemon and 'tsc -watch' with tsnode since they take up one terminal each to run. 
# #Or need to find a way of running 'tsc -watch' with nodemon.

# FROM prod as dev

# ENV NODE_ENV=development

# CMD [ "node","dist/index.js"]