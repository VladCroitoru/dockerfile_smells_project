# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
#FROM node:10.8.0  as build-stage
#WORKDIR /app
#COPY package*.json /app/
#RUN npm install
#COPY ./ /app/
#RUN npm run build -- --output-path=./dist/out --prod

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:latest
#FROM trion/nginx-angular
#Copy ci-dashboard-dist
#COPY --from=build-stage /app/dist/out/ /usr/share/nginx/html
COPY dist/intact-portal-view /usr/share/nginx/html/
#Copy default nginx configuration
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
