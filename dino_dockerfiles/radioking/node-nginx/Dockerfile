FROM node:alpine

RUN apk update && \
    apk add nginx
    
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
