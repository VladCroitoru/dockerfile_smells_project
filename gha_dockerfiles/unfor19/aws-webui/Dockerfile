### ---------------------------------------------------
### Global Arguments
### ---------------------------------------------------
ARG NODE_VERSION="14"
ARG ALPINE_VERSION="3.14"
### ---------------------------------------------------


### ---------------------------------------------------
### Build the application
### ---------------------------------------------------
FROM node:${NODE_VERSION}-alpine${ALPINE_VERSION} as build

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json yarn.lock ./
RUN  yarn install

# Build app
COPY . .
RUN  yarn build
### ---------------------------------------------------


### ---------------------------------------------------
### Server running the application
### ---------------------------------------------------
FROM node:${NODE_VERSION}-alpine${ALPINE_VERSION} as server

# Create server directory
WORKDIR /app/server/

# Install server dependencies
COPY server/package.json server/yarn.lock ./
RUN  yarn install

# Copy server code
COPY server ./

# Copy app dist
WORKDIR /app/dist/
COPY    --from=build /usr/src/app/dist/ .

# This is only a declaration, it is used only when executing `docker run -P unfor19/aws-webui` on Linux OS
EXPOSE  8080

# To use the scripts in package.json
WORKDIR /app/
COPY package.json .

# Serve the application in production mode
CMD [ "yarn", "serve:prod" ]
### ---------------------------------------------------
