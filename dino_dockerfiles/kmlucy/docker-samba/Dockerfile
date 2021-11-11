FROM alpine:3.6
LABEL maintainer "Kyle Lucy <kmlucy@gmail.com>"

COPY start.sh /start.sh

RUN apk add --no-cache samba samba-common-tools && chmod +x /start.sh

EXPOSE 139 445

CMD ["/start.sh"]
