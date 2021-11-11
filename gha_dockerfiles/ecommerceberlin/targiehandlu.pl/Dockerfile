FROM node:alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app
RUN npm run build
EXPOSE 3000
CMD [ "npm", "start" ]


#https://medium.com/google-cloud/next-js-tutorial-deploy-to-docker-on-google-cloud-container-engine-6b0c19dd8ecb
 
