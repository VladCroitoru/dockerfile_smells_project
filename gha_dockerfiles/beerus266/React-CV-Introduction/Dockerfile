###### build stage
FROM node:13-alpine as build-stage
# Create a directory in docker /app and cd to it
WORKDIR /app                
COPY . .
RUN npm install
RUN npm run build

##### production stage
FROM nginx:1.17-alpine as production-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]