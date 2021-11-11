# specify a base image the latest node alpine image
FROM node:16-alpine3.11

# Work directory is not specified in node v15 <= x
WORKDIR /usr/app

# copy the current directory into /usr/app
COPY ./package.json ./

# install some dependencies
RUN npm install

# copy rest of the files
COPY ./ ./

# set a default command
CMD ["npm","start"]
