FROM node:8

ENV DB_URI mongodb://mongo/bizumie
ENV URL http://localhost:3001

WORKDIR /opt/bizumie-oauth
COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 80

CMD npm start
