FROM node:boron

COPY package.json .

RUN npm install

# Bundle app source
COPY . .

EXPOSE 3001

CMD [ "npm", "start" ]