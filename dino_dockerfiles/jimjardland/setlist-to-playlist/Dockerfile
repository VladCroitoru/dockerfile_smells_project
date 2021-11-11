FROM node:8.4.0

RUN mkdir -p /www
WORKDIR /www

COPY package.json /www/
RUN npm install

COPY . /www

CMD ["npm", "start"]