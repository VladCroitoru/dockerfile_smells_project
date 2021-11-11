FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

EXPOSE 8000

ENTRYPOINT [ "npm", "start" ]