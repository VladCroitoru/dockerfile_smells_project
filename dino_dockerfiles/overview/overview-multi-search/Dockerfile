# Download a program for dev mode
FROM adamhooper/in-memory-website-http-server as http-server

# common: base image
FROM alpine:3.7 AS development

ENV PORT 80
EXPOSE 80
WORKDIR /app

# nodejs: compile website to flat file
# inotify-tools: watch for writes to flat file
RUN apk --update --no-cache add \
      inotify-tools \
      nodejs \
      nodejs-npm
COPY --from=http-server /usr/bin/in-memory-website-http-server /usr/bin/

# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:
COPY package.json package-lock.json /app/
RUN npm install

COPY webpack.config.js /app/

## We read files from here:
# (these are commented out because they break Docker Hub's auto-builder. TODO
# stop auto-building on Docker Hub so we can set target=production)
#VOLUME /app/app
#VOLUME /app/test

ENV PATH "/app/node_modules/.bin:/usr/local/bin:/usr/bin:/bin:/sbin"

# build: similar to development, bug saves /app/website.data
FROM development AS build

COPY . /app/
RUN node_modules/.bin/webpack


# production: web server
FROM adamhooper/in-memory-website-http-server AS production

COPY --from=build /app/website.data /website-data.in-memory-website
