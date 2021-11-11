FROM node:14.5.0-alpine

WORKDIR /usr

COPY package.json ./
COPY tsconfig.json ./

COPY src ./src
RUN npm install

EXPOSE 3001

CMD ["npm","run","dev"]