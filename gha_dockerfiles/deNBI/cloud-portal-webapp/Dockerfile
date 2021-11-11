### STAGE 1: Build ###

# We label our stage as 'builder'
FROM node:14-alpine3.10 as builder


COPY package.json  ./

RUN npm set progress=false && npm config set depth 0 && npm cache clean --force

RUN apk update && apk upgrade && apk add --no-cache bash git openssh
## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app

WORKDIR /ng-app

COPY . .

## Build the angular app in production mode and store the artifacts in dist folder
RUN $(npm bin)/ng build --configuration=custom   --build-optimizer

### STAGE 2: Setup ###
FROM nginx:1.21.3-alpine

## Copy our default nginx config
COPY nginx/default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

RUN mkdir -p /usr/share/nginx/html/portal/webapp
## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /ng-app/dist /usr/share/nginx/html/portal/webapp

CMD ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/portal/webapp/static/webapp/assets/environment/env.template.js> /usr/share/nginx/html/portal/webapp/static/webapp/assets/environment/env.js && exec nginx -g 'daemon off;'"]
