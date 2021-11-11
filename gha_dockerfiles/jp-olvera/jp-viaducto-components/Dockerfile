FROM node:12-stretch


WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 6006

CMD ["npm", "run", "start"]