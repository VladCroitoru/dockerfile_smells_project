FROM node:14 as BUILD
WORKDIR /build

COPY package-lock.json package.json ./
RUN npm install
COPY . ./
RUN npm run-script build


FROM nginx:alpine as SERVE

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=BUILD /build/dist /usr/share/nginx/html


FROM SERVE as VALIDATE_NGINX
# Check Nginx config syntax
RUN /usr/sbin/nginx -t -c /etc/nginx/nginx.conf
