#Specify a base image
FROM node:alpine

#Specify a working directory
WORKDIR /usr/src/app

#Copy the dependencies file
COPY ./package.json ./

#Install dependencies
RUN npm install --only=production

EXPOSE 8080

#Default command
CMD ["npm","start"]

#Copy remaining files
COPY ./ ./
