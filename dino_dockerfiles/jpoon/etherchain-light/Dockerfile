FROM node:6.11.3
WORKDIR /usr/src/app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
EXPOSE 3000

CMD [ "npm", "start" ]