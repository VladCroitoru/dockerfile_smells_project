FROM node:16.10.0

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}

RUN mkdir -p /app
WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm -v
RUN npm install

COPY . .

RUN npm run prisma:gen

EXPOSE 7777
CMD [ "node", "src/server.js" ]