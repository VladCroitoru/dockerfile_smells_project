
# Use the official lightweight Node.js 12 image.
# https://hub.docker.com/_/node
FROM node:lts-alpine

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure copying both package.json AND package-lock.json (when available).
# Copying this first prevents re-running npm install on every code change.
COPY package*.json ./

# Install production dependencies.
# If you add a package-lock.json, speed your build by switching to 'npm ci'.
# RUN npm ci --only=production
RUN npm ci

# Copy local code to the container image.
COPY . ./

# build
RUN npm run build

EXPOSE 3000

# Run the web service on container startup.
CMD [ "npm", "start" ]
