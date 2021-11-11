#TODO https://github.com/GoogleContainerTools/distroless
FROM node:16-alpine

WORKDIR /usr/src/action

COPY . .

RUN npm ci

ENTRYPOINT ["node", "/usr/src/action/index.mjs"]
