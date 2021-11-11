FROM mhart/alpine-node:latest

WORKDIR /src

COPY package*.json ./

RUN yarn install

COPY . .

RUN yarn tsbuild

EXPOSE 9000

CMD ["npm","start"]
