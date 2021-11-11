FROM node:14
# Create app directory
WORKDIR /usr/src/living
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install

# Bundle app source
COPY ./lib .

EXPOSE 3132

CMD [ "node", "src/utility/start.js" ]