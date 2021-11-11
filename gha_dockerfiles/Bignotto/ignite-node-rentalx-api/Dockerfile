FROM node

WORKDIR /usr/app

COPY package.json ./

RUN npm instal

COPY . .

EXPOSE 3333

CMD [ "npm","run","dev" ]