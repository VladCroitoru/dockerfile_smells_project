FROM alpine

RUN apk --update add --no-cache bash ca-certificates mailcap curl \
    && curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

EXPOSE 8080

COPY .docker.json /.filebrowser.json

ENTRYPOINT [ "filebrowser" ]
