FROM node:lts-alpine as builder
COPY . /app
WORKDIR /app
RUN npm install --production

FROM gcr.io/distroless/nodejs
COPY --from=builder /app /app
WORKDIR /app
EXPOSE $PORT
CMD ["index.js"]