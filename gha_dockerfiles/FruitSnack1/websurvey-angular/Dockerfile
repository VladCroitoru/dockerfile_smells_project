
FROM node:12.16.1-alpine As builder

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build --prod


FROM nginx:1.17.1-alpine
COPY nginx.conf /etc/nginx/nginx.conf
# COPY /dist/websurvey /usr/share/nginx/html
COPY --from=builder /usr/src/app/ssl/cert.crt /usr/share/nginx
COPY --from=builder /usr/src/app/ssl/cert.key /usr/share/nginx
COPY --from=builder /usr/src/app/dist/websurvey/ /usr/share/nginx/html
