FROM node:latest

# Setting working directory. All the path will be relative to WORKDIR
WORKDIR /usr/src/app

# Installing dependencies
COPY package*.json ./
COPY yarn.lock ./
RUN yarn install

# Copying source files
COPY . .

# Building app
RUN yarn run build

# Running the app
CMD [ "yarn", "start" ]