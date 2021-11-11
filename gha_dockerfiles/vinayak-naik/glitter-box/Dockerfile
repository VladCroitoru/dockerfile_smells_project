FROM node:14

# Create app directory
WORKDIR /app

# Install app dependencies
COPY package.json ./
COPY yarn.lock ./

RUN yarn

# Copying rest of the application to app directory
COPY . /app

# Expose the port and start the application
EXPOSE 8080

CMD ["yarn","start"]