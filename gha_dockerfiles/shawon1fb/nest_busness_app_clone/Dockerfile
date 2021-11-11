#define the latest nodejs image  to build from
FROM node:14.18

#install git
#RUN apk add --no-cache git

# create working folder and give permission
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

#create a working directory
WORKDIR /home/node/app

#copy package.json file under the working directory
COPY package*.json ./
COPY . .

RUN chown -R node:node /home/node/app/start.sh

# install all the dependencies
USER node


RUN yarn install
#copy all your files under the working directory
#start nodejs server
EXPOSE 8080
CMD [ "npm", "start" ]
#ENTRYPOINT [ "/home/node/app/start.sh" ]