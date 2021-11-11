FROM node:boron

# Create app directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Install dependencies
COPY package.json /usr/src/app
RUN npm install

# Add app-source
COPY . /usr/src/app

ENV PORT 80
CMD ["npm", "start"]
