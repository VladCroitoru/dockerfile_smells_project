FROM node:10-alpine as builder

# install and cache app dependencies
COPY package.json package-lock.json ./
RUN npm install --only=prod && mkdir /app && mv ./node_modules ./app

WORKDIR /app

COPY . .

RUN npm run build

# ------------------------------------------------------
# Production Build
# ------------------------------------------------------
FROM nginx:1.16.0-alpine
COPY --from=builder /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
