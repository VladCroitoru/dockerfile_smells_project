# BUILD STAGE
FROM node:16-alpine as builder

WORKDIR /app

COPY package*.json .

RUN apk --no-cache add --virtual native-deps \
  g++ gcc libgcc libstdc++ linux-headers make python && \
  npm install --quiet node-gyp -g && \
  npm install --quiet && \
  apk del native-deps

COPY . .

RUN npm run build

# PRODUCTION STAGE
FROM nginx:stable-alpine as production

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]