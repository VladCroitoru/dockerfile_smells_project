FROM node:14.17.4
RUN mkdir -p /app
WORKDIR /app

COPY package*.json ./
COPY tsconfig.json ./
COPY src /app/src

RUN npm install
RUN npm install -g pm2
RUN npm run build
COPY . .

EXPOSE 3000

CMD [ "pm2-runtime", "start", "serversystem.config.js"]