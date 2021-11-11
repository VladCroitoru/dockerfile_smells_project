FROM node:14-alpine

COPY package*.json ./
RUN npm install
COPY . .

CMD ["npx", "jest"]
