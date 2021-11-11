# Stage 1: Build an Angular Docker Image
FROM node:latest as build_stage
WORKDIR /app
COPY . /app/
RUN npm install
RUN npm run build --prod

# Stage 2, use the compiled app, ready for production with Nginx
FROM nginx:latest
COPY --from=build_stage /app/dist/todo-ui /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]