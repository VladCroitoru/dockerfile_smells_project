### STAGE 1: Build ###

# Build and compile app
FROM node:14 as build
MAINTAINER Roger Schaer <roger.schaer@hevs.ch>

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json ./
COPY yarn.lock ./
RUN yarn
RUN yarn global add react-scripts

# Copy app source
COPY . /usr/src/app

# Run the build
RUN yarn run build

### STAGE 2: Production Environment ###

# Deploy on the web server
FROM nginx:alpine

# Copy build files to HTML directory of nginx
COPY --from=build /usr/src/app/build /usr/share/nginx/html

# Copy nginx conf for dealing with routes
COPY ./react.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
