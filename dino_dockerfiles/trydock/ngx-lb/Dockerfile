FROM alpine:latest

RUN apk update && apk add nginx bash ca-certificates curl openssl git

RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443 8089

STOPSIGNAL SIGQUIT

# CMD ["nginx", "-g", "daemon off;"]
CMD ["nginx", "-g", "pid /tmp/nginx.pid; daemon off;"]
