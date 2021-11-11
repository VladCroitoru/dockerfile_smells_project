FROM node:16

WORKDIR /dist

COPY ./ ./

RUN npm install --only=prod

CMD ["npm", "start"]