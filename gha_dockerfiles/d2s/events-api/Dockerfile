# ---------------------------------------------------------
# Based on the:
# - Minimal Node.js Docker Images built on Alpine Linux
#   - https://github.com/mhart/alpine-node
FROM mhart/alpine-node:16 as builder

# Set one or more individual labels
LABEL name "d2s/events-api"
LABEL vendor="autiomaa.org"
LABEL org.autiomaa.version="0.0.1-beta"
LABEL org.autiomaa.release-date="2018-02-03"
LABEL org.autiomaa.version.is-production=""

# If you have native dependencies, you'll need extra tools
# RUN apk add --no-cache make gcc g++ python

# Create directories
RUN mkdir /app
WORKDIR /app

# Copy relevant files
COPY package.json package-lock.json /app/

# Install dependencies from npm packages
RUN npm install --production


# ---------------------------------------------------------
# Multi-stage build
# - https://docs.docker.com/develop/develop-images/multistage-build/

# Smaller base image (without npm or yarn)
FROM mhart/alpine-node:base-8 as production

# Copy over node_modules, etc
# from previous stage to the smaller base image
WORKDIR /app
COPY --from=builder /app .


# Copy application's source code itself
COPY src/ /app/src

# Choose what port to open up to the world
EXPOSE 3000

# Start the application itself
CMD ["npm", "start"]
