FROM nginx:alpine

RUN apk update && apk upgrade

RUN apk add --upgrade --no-cache openssl

COPY entrypoint.sh /entrypoint.sh

EXPOSE 80

CMD ["/entrypoint.sh"]
