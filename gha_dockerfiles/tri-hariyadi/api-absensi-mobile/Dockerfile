# FROM node:14-alpine
# ENV NODE_ENV=production
# WORKDIR /usr/src/app
# COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
# RUN npm install --production --silent && mv node_modules ../
# COPY . .
# EXPOSE 80
# RUN chown -R node /usr/src/app
# USER node
# CMD ["npm", "start"]

FROM node:14-alpine
WORKDIR /app
COPY package*.json /app
RUN npm install
COPY . /app
EXPOSE 8082
CMD [ "node", "app.js" ]
