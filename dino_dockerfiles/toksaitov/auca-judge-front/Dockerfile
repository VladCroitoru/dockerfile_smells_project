FROM node:4.4.4-slim

EXPOSE 8080
WORKDIR /auca-judge-front

COPY package.json /auca-judge-front
RUN npm install

COPY . /auca-judge-front

CMD ["npm", "start"]
