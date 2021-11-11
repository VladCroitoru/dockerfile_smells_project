FROM node:latest
WORKDIR /twice
COPY package*.json ./
RUN npm install -g --production
COPY . .
CMD ["node", "app.js"]
