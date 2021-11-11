# Image we're building from
FROM node:14-alpine
# Sets environment for subsequent builds
WORKDIR /app
# Caches node_modules. Removing this causes to install dependencies each time image is built.
ENV PATH /app/node_modules/.bin:$PATH
# Copy from root
COPY package.json yarn.lock ./
# Installs dependencies from package.json
RUN yarn
# Copy current directory to the workdir in the image
COPY . ./
# Builds project
RUN yarn build
