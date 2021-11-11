FROM node:8.1.0-alpine

MAINTAINER Paapa Abdullah Morgan <paapaabdullahm@gmail.com>

ENV PUBLIC_HOST=http://web.example.dev

RUN apk update \
    && apk add --update alpine-sdk \
    && apk add --update curl \
    && npm install -g @angular/cli@1.1.1 \
    && ng set --global packageManager=yarn \
    && mkdir -p /MyApp \
    && chmod 777 -R /MyApp \
    && apk del alpine-sdk \
    && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
    && npm cache --force clear \
    && sed -i -e "s/bin\/bash/bin\/sh/" /etc/passwd

WORKDIR /MyApp
EXPOSE 4200

CMD ["sh", "-c", "ng serve --host 0.0.0.0 --public-host ${PUBLIC_HOST}"]
