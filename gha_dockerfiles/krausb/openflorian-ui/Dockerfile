FROM node:8

WORKDIR /usr/src/app

COPY package*.json ./
COPY install.sh ./

RUN chmod +rx install.sh && ./install.sh

# Bundle app source
COPY . .

RUN npm run build

ENV NODE_ENV=production
ENV PORT=8080

EXPOSE 8080

CMD [ "/usr/local/bin/node", "server/index.js" ]
