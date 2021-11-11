FROM debian:wheezy
RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*
RUN echo "<h1>Curso Docker V2</h1>" > /usr/share/nginx/www/index.html

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]

