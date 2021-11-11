FROM gliderlabs/alpine:3.2

RUN ["apk-install", "darkhttpd"]
ADD . /var/www/

CMD darkhttpd /var/www --port ${PORT:-80}
