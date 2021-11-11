FROM node:lts-alpine

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm i --production

COPY . .

EXPOSE 8080

CMD ["node","index.js"]