FROM node:12-alpine
EXPOSE 3000


# Create work directory
WORKDIR /usr/src/app


# Copy app source to work directory
COPY . /usr/src/app

# Install app dependencies
RUN npm install

# Build and run the app
CMD npm run start:docker