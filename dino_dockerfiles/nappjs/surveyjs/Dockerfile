FROM nginx:alpine

COPY ./static /usr/share/nginx/html
COPY entrypoint.sh /entrypoint.sh

RUN apk add --update libintl

CMD [ "sh", "/entrypoint.sh" ]
