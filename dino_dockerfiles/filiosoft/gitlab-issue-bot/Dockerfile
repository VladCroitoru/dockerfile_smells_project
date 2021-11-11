FROM node:alpine

# Change working directory
WORKDIR /src

ENV NODE_ENV=production

# Copy package files
COPY package.json /src
COPY package-lock.json /src

# Install npm dependencies
RUN npm install

# Copy project files
COPY . /src

# Run application
CMD npm start