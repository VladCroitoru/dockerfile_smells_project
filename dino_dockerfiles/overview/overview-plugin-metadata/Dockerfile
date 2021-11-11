# Download an executable
FROM adamhooper/in-memory-website-http-server as in-memory-website


# development: gives Node and a dev loop
FROM alpine:3.7 as development

WORKDIR /app
EXPOSE 80

# nodejs: compile website to flat file
# inotify-tools: watch for writes to flat file
RUN apk add --update --no-cache \
      nodejs \
      nodejs-npm \
      inotify-tools
COPY --from=in-memory-website /usr/bin/in-memory-website-http-server /usr/bin/

COPY package.json package-lock.json /app/
RUN npm install

## We read files from here:
# (these are commented out because they break Docker Hub's auto-builder. TODO
# stop auto-building on Docker Hub so we can set target=production)
# VOLUME /app/assets
# VOLUME /app/config
# VOLUME /app/generator
# VOLUME /app/views


# build: outputs /app/website.data
FROM development AS build

COPY . /app/
RUN generator/build.js > /app/website.data


# production: serves the website
FROM adamhooper/in-memory-website-http-server as production

COPY --from=build /app/website.data /website-data.in-memory-website
