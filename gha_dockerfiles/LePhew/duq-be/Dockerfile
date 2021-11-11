# Use the official lightweight Node.js 12 image.
# https://hub.docker.com/_/node
FROM node:12-alpine as build

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure both package.json AND package-lock.json are copied.
# Copying this separately prevents re-running npm install on every code change.
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy local code to the container image.
COPY . ./

# Build the application
RUN npm run build

FROM node:12-alpine as prod

WORKDIR /usr/src/app

COPY --from=build /usr/src/app/dist ./
COPY --from=build /usr/src/app/node_modules/ ./node_modules

# Run the web service on container startup.
CMD [ "node", "main.js" ]