FROM node:16-alpine

WORKDIR /app
COPY . .

RUN npm i
RUN npm run generate:dev

RUN chmod +x ./entrypoint.dev.sh

EXPOSE 3000
CMD ["npm", "run", "start:dev"]