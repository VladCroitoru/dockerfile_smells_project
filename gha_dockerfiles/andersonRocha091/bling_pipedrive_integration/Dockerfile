FROM node:12.18.3-alpine3.11
# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["sh", "-c", "npm run ${node_env}"]
