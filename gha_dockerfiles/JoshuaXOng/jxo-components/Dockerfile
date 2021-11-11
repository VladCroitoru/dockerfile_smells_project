FROM node:14

WORKDIR /jxo-components

COPY package*.json ./

RUN npm install

COPY ./ ./

# Don't forget to port-foward (-p) when creating the container.
EXPOSE 8080

CMD ["npm", "start"]