FROM node:lts-alpine
WORKDIR /app/
COPY package.json package-lock.json /app/
RUN npm install --production
COPY . /app/
CMD node index.js
