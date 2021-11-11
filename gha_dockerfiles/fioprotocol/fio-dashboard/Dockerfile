FROM node:14.17.4

WORKDIR /usr/app

COPY package.json /usr/app/
RUN npm install

COPY . .

EXPOSE 9000
CMD ["npm", "run", "server:dev"]
