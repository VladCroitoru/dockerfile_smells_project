FROM node

RUN mkdir -p /app

COPY . /app

WORKDIR /app

COPY package.json /app

RUN npm install

EXPOSE 5000 80 443

CMD npm start
