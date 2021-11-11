FROM node:10

WORKDIR /usr/app

COPY package.json .

RUN npm i --quiet

RUN npm install pm2 -g

COPY . .

EXPOSE 8080

CMD ["pm2-runtime", "index.js"]