FROM node:16
WORKDIR /app

RUN apt-get update && \
  apt-get install -y --no-install-recommends ffmpeg build-essential python libfontconfig1 dumb-init git

RUN curl -f https://get.pnpm.io/v6.16.js | node - add --global pnpm

# Files required by pnpm install
COPY package.json pnpm-lock.yaml ./

RUN pnpm fetch
RUN pnpm install

# Bundle app source
COPY . .
CMD ["pnpm", "run", "start:dev"]
