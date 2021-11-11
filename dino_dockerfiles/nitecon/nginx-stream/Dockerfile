FROM nginx:latest

RUN echo 'include /etc/nginx/stream.d/*.conf;' >> /etc/nginx/nginx.conf

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]