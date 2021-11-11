# https://mherman.org/blog/dockerizing-a-react-app/
FROM node:14.17-alpine as development
WORKDIR /agoracloud
ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine as production
COPY --from=development /agoracloud/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]