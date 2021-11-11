## Dockerfile for creating a production image
FROM node:16-alpine3.11 as builder



#########################
# BACKEND NODE PACKAGES #
#########################

# Change working directory to backend
WORKDIR /backend

COPY [ "./backend/package.json", "./backend/package-lock.json", "./" ]

# Only the production packages are needed
ENV NODE_ENV production

# Make a clean install of node packages which are needed for production
RUN npm install

# Install and run node-prune. It deletes unnecessary files from node_modules, such as md files etc
RUN apk update && apk add curl bash && rm -rf /var/cache/apk/*
RUN curl -sfL https://install.goreleaser.com/github.com/tj/node-prune.sh | bash -s -- -b /usr/local/bin
RUN /usr/local/bin/node-prune



##########################
# FRONTEND NODE PACKAGES #
##########################
# Generate the static files with webpack

# Create a folder for frontend building and set current directory to it
WORKDIR /frontend

# Copy package files from frontend folder into our new working directory in our image
COPY [ "./frontend/package.json", "./frontend/package-lock.json", "./" ]

ENV NODE_ENV development

# Install all packages required for building the frontend. which includes dev-dependencies
RUN npm install



##################
# BUILD FRONTEND #
##################
# This is done separate from installing node pakcages
# Each COPY creates a new layer. And if that layer has changed from previous builds, all subsequent ones have to be rebuilt!
# Hence I start with the one which is changed least frequently

# Copy all frontend code into /frontend-building directory inside the container
COPY ./frontend .

# Build the frontent with webpack. All files will be built inside /build
RUN npm run build



###############
# FINAL BUILD #
###############
# Copy over static frontend files
# Copy over backend source code
# Copy over installed node packages for backend

## This FROM will start a new container
FROM node:16-alpine3.11

WORKDIR /app

COPY --from=builder /frontend/build /app/build
COPY ./backend/src /app/src
COPY --from=builder /backend/node_modules /app/node_modules

ENV NODE_ENV production

EXPOSE 3000

CMD [ "node", "./src/index.js" ]