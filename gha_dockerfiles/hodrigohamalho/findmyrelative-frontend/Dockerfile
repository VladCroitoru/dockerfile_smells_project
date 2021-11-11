FROM node:12-alpine

COPY . .

RUN npm install && \
    npm run build

EXPOSE 8080
CMD npm run start
