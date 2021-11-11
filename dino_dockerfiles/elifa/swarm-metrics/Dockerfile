FROM node:alpine

WORKDIR /usr/src/app

ENV REGION="" \
    STACK_NAME="" \
    INSTANCE_NAME="" \
    INTERVAL=10 \
    NAMESPACE="Swarm"

COPY package.json ./
RUN npm install

COPY . .

CMD [ "npm", "run", "start" ]
