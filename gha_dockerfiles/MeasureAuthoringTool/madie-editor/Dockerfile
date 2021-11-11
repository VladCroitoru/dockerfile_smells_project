FROM node:16 as build-stage
WORKDIR /usr/src/app
COPY . .
RUN npm install && \
    npm run build:webpack && \
    npm test -- --silent

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.21.0-alpine
COPY --from=build-stage /usr/src/app/dist/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8501