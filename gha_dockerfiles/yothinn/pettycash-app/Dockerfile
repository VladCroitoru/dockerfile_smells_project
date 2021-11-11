### STAGE 1: Build ###

# We label our stage as 'builder'
FROM node:10-alpine as builder
ARG NODE_ENV
ARG API_BASE_URL
ENV NODE_ENV "$NODE_ENV"
ENV API_BASE_URL "$API_BASE_URL"

COPY package.json package-lock.json ./
RUN npm set progress=false && npm config set depth 0 && npm cache clean --force
RUN npm install -g ts-node yargs dotenv typescript

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
RUN npm i && mkdir /ng-app && cp -R ./node_modules ./ng-app
WORKDIR /ng-app
COPY . .
## Build the angular app in production mode and store the artifacts in dist folder
RUN ts-node ./scripts/set-env.ts --environment=prod 
#actually this is defined as a script in package.json, let's add it here so things would make sense.
RUN npm run build


### STAGE 2: Setup ###

FROM nginx:1.13.3-alpine
## Clear All .Conf All
RUN rm /etc/nginx/conf.d/*
## Copy our default nginx config
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY --from=builder /ng-app/dist /usr/share/nginx/html
# CMD ["nginx", "-g", "daemon off;"]
COPY --from=builder /ng-app/scripts/replace_api_url.sh /

CMD ["sh", "replace_api_url.sh"]