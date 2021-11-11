# Configuration to build an nginx container
# for serving Django apps on the same kubernetes pod

FROM nginx:latest

VOLUME ["/mnt/static", "/mnt/media"]
COPY nginx.conf /etc/nginx/nginx.conf
