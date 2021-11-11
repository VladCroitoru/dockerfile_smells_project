# Stage 1: Compile and Build angular codebase

# Use official node image as the base image
FROM node:latest as build

# Set the working directory
WORKDIR /usr/local/app

# Add the source code to app
COPY ./ /usr/local/app/

# Install all the dependencies
RUN npm install

# Generate the build of the application
RUN npm run build


# Use official node image as the base image
FROM node:alpine

RUN apk add dumb-init

WORKDIR /usr/local/app

# Copy the build output to replace the default nginx contents.
COPY --from=build /usr/local/app/webpack/api.bundle.js ./

# Copy the static assets over into the dist file
COPY --from=build /usr/local/app/dist ./dist

RUN mkdir /certs && ln -s /etc/letsencrypt/live/mattandclaire.net /usr/local/app/certs

# Expose port 80
EXPOSE 80

# Run
CMD ["dumb-init", "node", "api.bundle.js" ]
