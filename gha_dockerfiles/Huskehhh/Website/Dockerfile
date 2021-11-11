FROM node:current-alpine3.12 as builder
WORKDIR /app
COPY . .
RUN npm i
RUN npm run build

FROM nginx:stable-alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
