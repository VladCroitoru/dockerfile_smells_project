FROM alpine:latest

MAINTAINER david <golucky@gmail.com>

RUN apk --update add git \
        nginx
RUN rm -rf /usr/share/nginx/html/*.*
RUN git clone https://github.com/golucky5/CaveRunner.git /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
