FROM node:14-alpine3.11

# set target folder for app
WORKDIR /usr/src/api

# ENV NODE_ENV production
ENV NODE_ENV development

# need packages to get started
COPY package*.json /usr/src/api

# update all the packages in node_modules
RUN npm install 
# RUN npm install && npm install nodemon

# move code from repo to container
COPY . .

EXPOSE 5555

# allow browser connection to docker
CMD ["npm", "run", "start"]


