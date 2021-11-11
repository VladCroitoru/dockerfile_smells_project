FROM node:8.1.3-slim

EXPOSE 7474
WORKDIR /morse-back

COPY package.json /morse-back
RUN npm install

COPY . /morse-back

CMD ["npm", "start"]

