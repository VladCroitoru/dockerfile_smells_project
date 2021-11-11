# Dockerfile

FROM node:8-alpine

WORKDIR /usr/src/app

COPY package.json .

RUN npm install

# Bundle app source
COPY . .

RUN npm run build

EXPOSE 3000

CMD [ "npm", "run", "prod" ]
