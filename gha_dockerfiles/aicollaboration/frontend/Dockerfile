# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:12.0 as build-stage
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app/
ARG configuration=production
RUN npm run build:prod:mem -- --output-path=./dist/out --configuration $configuration

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15
#Copy ci-dashboard-dist
COPY --from=build-stage /app/dist/out/ /usr/share/nginx/html
#Copy default nginx configuration
COPY ./deployment/configs/nginx-custom.conf /etc/nginx/conf.d/default.conf
EXPOSE 80