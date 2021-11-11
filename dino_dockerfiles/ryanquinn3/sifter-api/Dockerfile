FROM node:7.7.1

WORKDIR /code/

COPY yarn.lock .
COPY package.json .

RUN yarn

COPY . .

EXPOSE 5000

CMD ["npm", "start"]

