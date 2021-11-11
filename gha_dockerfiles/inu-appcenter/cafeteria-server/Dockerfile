FROM node:14

WORKDIR /opt/cafeteria-server

COPY . .

RUN npm ci

EXPOSE 20201-20202

CMD ["npm", "start"]
