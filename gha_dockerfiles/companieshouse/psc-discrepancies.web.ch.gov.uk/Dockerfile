FROM node:14-alpine
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
CMD ["node", "server.js"]
EXPOSE 3000
