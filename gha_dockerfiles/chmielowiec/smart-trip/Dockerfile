# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:alpine as build-stage
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app/
#ARG configuration=production
RUN npm run build -- --output-path=./dist/out --configuration production

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:alpine
COPY --from=build-stage /app/dist/out/ /usr/share/nginx/html

# Copy the default nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'
