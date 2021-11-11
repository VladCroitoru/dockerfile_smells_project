FROM node:14.17.5
# FROM node:14-alpine3.11 ... axios issue
# set target folder for app
WORKDIR /usr/src
# need only packages to get started
COPY package*.json /usr/src/
# update all the packages in node_modules
RUN npm install && npm run build
# move code from repo to container
COPY . /usr/src
EXPOSE 3000
ENV HOST 0.0.0.0
# CMD ["npm", "run", "dev"]
