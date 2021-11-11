FROM node:14-alpine as builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY tsconfig.json ./
COPY src src
RUN npm run build

FROM node:14-alpine
ENV NODE_ENV=production
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY --from=builder /app/build ./build
ENTRYPOINT [ "node" ]
CMD [ "./build" ]