FROM node:12-alpine

RUN apk update && apk add python make g++ ffmpeg

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm -g install pnpm
RUN pnpm install

COPY . .

CMD ["pnpm", "start:dev"]