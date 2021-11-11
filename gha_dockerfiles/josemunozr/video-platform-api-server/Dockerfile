FROM node:12.18.3-alpine
WORKDIR /src/app
COPY ./package.json ./
RUN npm install
COPY . .
EXPOSE 3000
ENV NODE_ENV=production
CMD ["node", "index.js"]