# Use an official Node runtime as a parent image
FROM node:8.4.0

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages
RUN npm install
RUN npm run build

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NODE_ENV production

# Run npm start when the container launches
CMD ["npm", "start"]
