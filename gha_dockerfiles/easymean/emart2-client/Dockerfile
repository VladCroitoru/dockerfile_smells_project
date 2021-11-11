FROM node:14 as builder

WORKDIR /app
COPY emart2/package*.json ./
RUN npm ci
COPY emart2/ .
RUN npm install
RUN npm run build


FROM nginx:latest
EXPOSE 80
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html