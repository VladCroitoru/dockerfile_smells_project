FROM node:lts-alpine
RUN apk add g++ make python3
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn --frozen-lockfile
COPY . .
RUN yarn build
ENV HOST 0.0.0.0
ENTRYPOINT [ "yarn", "start" ]
