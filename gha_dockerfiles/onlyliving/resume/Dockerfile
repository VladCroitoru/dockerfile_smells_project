FROM node:15.14.0-alpine3.10

RUN mkdir /workspace

COPY package.json /workspace

WORKDIR /workspace

RUN apk add python make g++  && \
    npm install

COPY . /workspace/

RUN npm run build

ENTRYPOINT ["npx","serve", "dist", "-l", "tcp://0.0.0.0:80"]
