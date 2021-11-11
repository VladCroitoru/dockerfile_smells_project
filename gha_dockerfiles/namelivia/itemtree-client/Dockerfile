# base builder stage
FROM node:12-stretch as base-builder
WORKDIR /app
COPY package*.json ./
COPY . .

# build stage for development
FROM base-builder as development-builder
RUN npm install --also=dev

# build stage for production
FROM base-builder as production-builder
RUN npm install
RUN npm run build

# production stage
FROM nginx:stable-alpine as production
COPY --from=production-builder /app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# development stage
FROM development-builder as development
EXPOSE 8080
CMD ["npm", "run", "serve"]
