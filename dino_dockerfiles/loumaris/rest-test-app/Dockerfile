### STAGE 1: Build ###

# We label our stage as 'builder'
FROM node:8-alpine as builder


RUN npm set progress=false && \
    npm config set depth 0 && \
    npm cache clean --force && \
    mkdir /app

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build

RUN npm install -g @angular/cli

COPY . /app

WORKDIR /app

RUN npm install

## Build the angular app in production mode and store the artifacts in dist folder
RUN $(npm bin)/ng build --prod


### STAGE 2: Setup ###

FROM nginx:1.13.3-alpine

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
