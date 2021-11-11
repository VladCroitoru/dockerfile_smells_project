# Use following version of Node as the base image
FROM node:10-alpine

# Set work directory for run/cmd
WORKDIR /app

# Copy package.json and package-lock.json into work directory and install dependencies
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN npm install --production

# Copy everthing else in work directory
COPY . /app

# Expose server port
EXPOSE 3000

# Run node
CMD ["node", "/app/index.js"]
