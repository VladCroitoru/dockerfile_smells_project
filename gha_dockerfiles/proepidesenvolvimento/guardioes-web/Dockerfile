# Pull official base image
FROM node:10-alpine

# Set working directory
WORKDIR /code

# Copy all files to docker container
COPY . .

# Install app dependencies
RUN npm install
RUN npm install react-scripts -g
RUN npm install serve -g

# Load app into container
RUN npm run-script build

# Start app
CMD ["serve", "-s", "build"]

