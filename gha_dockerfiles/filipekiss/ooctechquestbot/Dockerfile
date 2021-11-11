FROM node:14
WORKDIR /app

COPY package*.json ./
RUN rm -rf node_modules
RUN npm ci 

COPY . .

RUN npm run build

CMD ["node", "dist/main.js"]
