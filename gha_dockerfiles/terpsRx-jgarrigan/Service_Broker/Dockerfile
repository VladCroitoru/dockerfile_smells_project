FROM node:12-alpine
# create the node_modules directory and make sure the app is owned by us
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
# set the working directory
WORKDIR /home/node/app
# copy our package and package-lock json files
COPY package*.json ./
# declare the user explicitly 
USER node
# copy our application to the container
COPY --chown=node:node . .
# build the application 
RUN npm install
# expose our application port
EXPOSE 80 443
# issue the run command
CMD [ "npm", "run", "start" ]