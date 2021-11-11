# Pull Docker Hub base image
FROM node:14.16.0-alpine3.10
# Set working directory
WORKDIR /usr/app
# Install app dependencies
COPY package*.json ./
RUN npm install -qyg nodemon@2.0.7
RUN npm install -qy
# Copy app to container
COPY . .
# Run the "dev" script in package.json
CMD ["npm", "run", "dev"]