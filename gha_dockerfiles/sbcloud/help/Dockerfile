FROM node:14.16.0

WORKDIR /app

RUN npm -g install gatsby-cli

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

CMD ["gatsby", "serve", "--verbose", "--prefix-paths", "-p", "8080", "--host", "0.0.0.0"]
