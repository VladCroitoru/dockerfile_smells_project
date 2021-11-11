FROM node:14-alpine

ENV TZ=America/Sao_Paulo
RUN mkdir -p /home/node/trabalho

WORKDIR /home/node/trabalho

COPY ./package.json ./
COPY ./src ./src

RUN npm install 

EXPOSE 3000

CMD [ "node", "./src/index.js" ]