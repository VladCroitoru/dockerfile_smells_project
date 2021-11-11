FROM node:7.10
WORKDIR /app

EXPOSE 8080

CMD ["npm", "start"]

COPY package.json /app
RUN npm install

COPY . /app
