FROM node:lts

WORKDIR /app

RUN chown node:node /app

COPY . .

RUN npm install -g nodemon
RUN npm install typescript -g
RUN npm install -g

USER node

EXPOSE 8100
RUN npm run start
