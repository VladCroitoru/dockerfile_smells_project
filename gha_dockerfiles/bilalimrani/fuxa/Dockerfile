FROM node:14

# Create app directory
WORKDIR /usr/src/app

RUN git clone https://github.com/frangoteam/FUXA.git
WORKDIR /usr/src/app/FUXA

# Install server
WORKDIR /usr/src/app/FUXA/server
RUN npm install

WORKDIR /usr/src/app/FUXA/server
EXPOSE 8080
CMD [ "npm", "start" ]