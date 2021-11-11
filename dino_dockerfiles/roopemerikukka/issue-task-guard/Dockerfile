FROM node:9.4.0

ENV NODE_ENV production

WORKDIR /app

COPY package.json /app
RUN npm install
COPY . /app

EXPOSE 3000

CMD ["npm", "start"]