FROM node:argon

# Create app directory
RUN mkdir -p /usr/src/eviewsSDMX
WORKDIR /usr/src/eviewsSDMX

# Install app dependencies
COPY package.json /usr/src/eviewsSDMX
RUN npm install

# Bundle app source
COPY . /usr/src/eviewsSDMX

EXPOSE 8080
CMD ["npm","start"]


