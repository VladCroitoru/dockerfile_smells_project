FROM node:4-alpine

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN npm install -g .

ENTRYPOINT [ "/usr/local/bin/annotate-uploader" ]
