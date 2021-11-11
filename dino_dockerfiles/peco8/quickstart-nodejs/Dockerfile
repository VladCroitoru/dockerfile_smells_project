# Using official php runtime base image
FROM node:argon

MAINTAINER "Toshiki Inami <t-inami@arukas.io>"

# Set the applilcation directory
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install app dependencies
COPY package.json $APP_HOME/
RUN npm install

# Copy our code from the current folder to /app inside the container
COPY . $APP_HOME

# Make port 3000 available for publish
EXPOSE 3000

# Start server
CMD [ "npm", "start" ]
