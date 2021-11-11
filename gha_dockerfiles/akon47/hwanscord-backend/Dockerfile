FROM node:14

WORKDIR /app

COPY ./package.json ./
RUN npm install
COPY src .
RUN mkdir avatar
RUN mkdir attachments

CMD ["node", "server.js"]
