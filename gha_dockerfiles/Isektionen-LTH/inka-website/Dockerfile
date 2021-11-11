FROM node:12

RUN npm install -g nodemon

WORKDIR /app
COPY . /app
RUN npm install

EXPOSE 3000

CMD npm start