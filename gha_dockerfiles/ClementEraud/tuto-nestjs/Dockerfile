# pull official base image
FROM node:14.0.0-alpine

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./ 
COPY package-lock.json ./

RUN npm install
COPY . ./

RUN npm run build

CMD ["node", "dist/main.js"]
