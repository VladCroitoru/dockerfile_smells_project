FROM alpine:latest
LABEL maintainer="gwaewion@gmail.com"
EXPOSE 80

RUN apk update
RUN apk add nginx git
RUN mkdir /run/nginx
COPY nginx.conf /etc/nginx/
RUN rm -rf /var/www/localhost
WORKDIR /var/www/
RUN git clone https://github.com/gwaewion/vetopytter-web.git .


WORKDIR /

CMD ["nginx", "-g", "daemon off;"]
