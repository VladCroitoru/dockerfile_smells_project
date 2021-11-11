FROM node:8.1.2-slim

EXPOSE 7373
WORKDIR /temperature-back

COPY package.json /temperature-back
RUN npm install

COPY . /temperature-back

CMD ["npm", "start"]

