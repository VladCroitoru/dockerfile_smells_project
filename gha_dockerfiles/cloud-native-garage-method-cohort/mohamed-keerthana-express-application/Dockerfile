FROM quay.io/ibmgaragecloud/node:lts-stretch

WORKDIR /usr/src/app

COPY . .

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]