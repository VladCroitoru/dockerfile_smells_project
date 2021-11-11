FROM node:12

# Create app directory
WORKDIR /usr/src/app

COPY tsconfig.json ./
COPY state.json ./
COPY app ./app
COPY package.json ./
COPY yarn.lock ./

RUN yarn

EXPOSE 2880

CMD [ "yarn", "start" ]
