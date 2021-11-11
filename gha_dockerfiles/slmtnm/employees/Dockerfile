FROM node:16-alpine3.11
LABEL Author="Makar Solomatin <makar.solomatin.5@yandex.ru>"
WORKDIR /app

COPY . .
RUN npm install

CMD ["node", "src/app.js"]
