FROM node:4.6.1

WORKDIR /app
COPY ./app.js ./package.json ./
RUN npm install
CMD node ./app.js

EXPOSE 3000
