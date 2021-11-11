FROM nginx:alpine
COPY src/docker/nginx.conf /etc/nginx/nginx.conf
WORKDIR /usr/share/nginx/html/cv-generator-fe
ONBUILD COPY dist/ .
