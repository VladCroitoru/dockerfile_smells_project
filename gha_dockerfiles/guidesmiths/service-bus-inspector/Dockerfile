FROM node:10.16

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY .npmrc package*.json ./
COPY react-app/package*.json ./react-app/

RUN npm install && cd react-app && npm install && cd ..
COPY . .
RUN cd react-app && npm run build && cd ..

# Bundle app source

EXPOSE 4000

RUN npm run manifest

CMD [ "npm", "start" ]

