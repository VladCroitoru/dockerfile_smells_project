FROM node

WORKDIR /app

COPY package.json ./

RUN npm i --only=production

COPY index.js .

ENV TZ Australia/Sydney

CMD ["node", "index.js"]

