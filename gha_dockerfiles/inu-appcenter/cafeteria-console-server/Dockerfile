FROM node:14

WORKDIR /opt/cafeteria-console-server

COPY . .

RUN npm ci

EXPOSE 40401-40402

CMD ["npm", "start"]
