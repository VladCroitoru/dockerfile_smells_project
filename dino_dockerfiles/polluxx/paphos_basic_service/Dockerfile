FROM node:latest

RUN mkdir /src

RUN npm install nodemon -g

COPY ./ /src
WORKDIR /src
RUN npm install

RUN chmod 755 /src/*.sh


EXPOSE 3002

CMD npm run hosts && npm start
