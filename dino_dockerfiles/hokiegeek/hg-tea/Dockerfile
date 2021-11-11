FROM nginx
RUN sed -i '/location \/ {/{n;n;s/.*/index index.html;\ntry_files $uri $uri\/ \/index.html =404;/}' /etc/nginx/conf.d/default.conf
COPY dist/ /usr/share/nginx/html/
