FROM node:alpine

WORKDIR /usr/alamin

COPY ./package.json ./
RUN npm install
COPY ./ ./

CMD ["npm", "start"]
