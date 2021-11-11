FROM node:13

# Create app directory in case of unexpected overwriting
WORKDIR /usr/src/app

# For cached node_modules
COPY package*.json ./

RUN npm install

COPY ./ ./

CMD ["npm", "run", "build"]

CMD ["npm", "run", "docker-start:prod"]