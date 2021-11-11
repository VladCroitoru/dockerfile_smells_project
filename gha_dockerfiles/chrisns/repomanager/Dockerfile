FROM node:17.0.1-alpine
WORKDIR /app
COPY . .

RUN npm install --production

USER node

CMD npm start