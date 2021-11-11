FROM node:lts-alpine

MAINTAINER Jonas aka Lord Maccyber

# Set args
ARG VUE_APP_AUTH_CLIENT_ID
ARG VUE_APP_ELEVMAPPA_API_URL
ARG VUE_APP_ELEVMAPPA_PROD_URL
ARG VUE_APP_AUTH_AUTHORITY

# Set envs
ENV VUE_APP_AUTH_CLIENT_ID $VUE_APP_AUTH_CLIENT_ID
ENV VUE_APP_ELEVMAPPA_API_URL $VUE_APP_ELEVMAPPA_API_URL
ENV VUE_APP_ELEVMAPPA_PROD_URL $VUE_APP_ELEVMAPPA_PROD_URL
ENV VUE_APP_AUTH_AUTHORITY $VUE_APP_AUTH_AUTHORITY

# install simple http server for serving static content
RUN npm install -g http-server-spa

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server-spa", "dist" ]
