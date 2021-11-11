FROM nginx
RUN rm /usr/share/nginx/html/*
COPY web usr/share/nginx/html
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
