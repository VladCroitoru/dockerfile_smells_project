# pull official base image
FROM node:13.12.0-alpine as builder

#!/bin/bash

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY yarn.lock ./

# Installs all node packages
RUN yarn install --no-optional --ignore-engines

# Copies everything over to Docker environment
COPY . ./
RUN yarn run build

#Stage 2
#######################################
#pull the official nginx:1.19.0 base image
FROM nginx:1.19.0
COPY nginx.conf /etc/nginx/conf.d/default.conf
#copies React to the container directory
# Set working directory to nginx resources directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static resources
RUN rm -rf ./*
# Copies static resources from builder stage
COPY --from=builder /app/build .
# Containers run nginx with global directives and daemon off
#ENTRYPOINT ["nginx", "-g", "daemon off;"]
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]