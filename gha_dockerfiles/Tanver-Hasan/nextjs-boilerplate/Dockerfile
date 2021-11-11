FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 80
CMD ["npm","start"]
