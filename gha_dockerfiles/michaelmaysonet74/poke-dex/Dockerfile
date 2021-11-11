FROM node:16-alpine

COPY . .

RUN npm i
RUN npm run compile

EXPOSE 4000

CMD ["node", "./dist/src/server.js"]
