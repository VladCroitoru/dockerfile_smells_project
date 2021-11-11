FROM node:16

WORKDIR /user-auth
COPY package.json .
RUN npm install
COPY . .
CMD npm start