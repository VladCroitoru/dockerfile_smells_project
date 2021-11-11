FROM node:14-alpine

# Set the app directory in the container
WORKDIR /usr/src/app

# Copy over packages
COPY package*.json ./

# Install packages in container
RUN yarn install

# Copy all source
COPY . .

EXPOSE 3000

# Run the command to start the container
CMD ["yarn", "run", "start:dev"]