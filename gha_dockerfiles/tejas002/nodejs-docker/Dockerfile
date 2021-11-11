# Pull the node image from docker hub
FROM node:12.18-alpine

#Setting environment variable
ENV NODE_ENV production

#Will set/create the working directory inside docker image
WORKDIR /usr/src/app

#Copy the package*.json in the  working directory inside docker image
COPY ["package.json", "package-lock.json*", "./"]

#Installing packages in working directory inside docker image
RUN npm install --production --silent && mv node_modules ../

#Copy all the file/folders from current directory to working directory
COPY . .

#Exposing the port for container
EXPOSE 9005

ENTRYPOINT ["npm"]
CMD ["start"]


# ***********************************************************************************
# Small size image will be generated , but cant fix the nodejs version? need to check

# FROM alpine:latest
# RUN apk add --no-cache nodejs npm
# WORKDIR /app/code
# COPY . .
# RUN npm install
# EXPOSE 9005
# ENTRYPOINT ["npm"]
# CMD ["start"]
