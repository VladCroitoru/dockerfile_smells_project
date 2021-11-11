# Create image based on the official Node 6 image from the dockerhub
FROM node

# Setting up environment variable
ENV PORT 3000

# Create a directory where our app will be placed
RUN mkdir -p /usr/apps/custom-badge

# Change directory so that our commands run inside this new directory
WORKDIR /usr/apps/custom-badge

# Copy dependency definitions
COPY package.json /usr/apps/custom-badge

# Install dependecies
RUN npm i

# Get all the code needed to run the app
COPY ./server.js /usr/apps/custom-badge

# Expose the port the app runs in
EXPOSE 3000

# Serve the app
CMD ["npm", "start"]
