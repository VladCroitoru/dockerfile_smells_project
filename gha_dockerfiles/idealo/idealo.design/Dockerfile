FROM node:14.16.1 

WORKDIR /home/node/app

COPY . ./
RUN npm config set color false
RUN npm ci
RUN npm run build

WORKDIR /home/node/app/dist

EXPOSE 8080

CMD ["node", "server.js"]
