FROM node:14 AS builder
WORKDIR /app
COPY ./package.json ./package-lock.json ./
RUN npm install
COPY ./nest-cli.json ./tsconfig.build.json ./tsconfig.json ./
ADD ./src ./src
ADD ./test ./test
ADD ./test_environment ./test_environment
RUN npm run build

FROM node:14-alpine
WORKDIR /app
COPY --from=builder /app ./
EXPOSE 3000
CMD ["npm", "run", "start:prod"]