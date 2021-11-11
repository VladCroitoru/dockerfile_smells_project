FROM node:8.4-alpine
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["node", "./lib/index.js"]
EXPOSE 3000