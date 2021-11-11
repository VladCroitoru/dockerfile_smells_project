FROM node:16.13.0

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]