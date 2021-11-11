# Using Node.js 8 LTS
FROM node:8-alpine

# Install git, required by some packages
RUN apk --no-cache add git

# Install global NPM packages for formatting and redirecting pino logs
RUN npm install --global pino pino-http pino-noir pino-tee pino-elasticsearch pino-mongodb

# Set workdir
WORKDIR /usr/src/app

# First, copy package.json and package-lock.json to run "npm install"
COPY ["package.json", "package-lock.json", "./"]
RUN npm install --production

# Copy the app
COPY . .

# Start the app
ENV NODE_ENV production
CMD npm run production
VOLUME /var/log/
EXPOSE 3000
