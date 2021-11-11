FROM node:alpine AS builder

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.19-alpine
COPY --from=builder /app/public /usr/share/nginx/html

# Copy .env file and shell script to container
WORKDIR /usr/share/nginx/html
COPY ./docker/env.sh .
COPY ./docker/.env .

# Add bash
RUN apk add --no-cache bash

# Make our shell script executable
RUN chmod +x env.sh

# Start Nginx server
CMD ["/bin/bash", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]