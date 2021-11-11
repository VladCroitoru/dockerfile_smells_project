FROM node:14-alpine

COPY . .

RUN npm install

ENV PORT=9000

ENTRYPOINT ["npm", "start"]
