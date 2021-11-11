FROM node:alpine as builder
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# /app/build <-- will have all the goodies necessary to run in prod

FROM nginx
EXPOSE 80
# expose is communication for developers to expose port map to port 80. Does nothing for us automatically.
# However with elastic beanstalk, it will look intot he docker file and look for the expose.
# Whatever port is exposed, it will expose it automatically
COPY --from=builder /app/build /usr/share/nginx/html

# server from nginx production server