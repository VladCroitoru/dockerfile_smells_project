FROM alpine:latest
RUN apk update \
    && apk add nodejs npm
COPY ./calculator /calculator
WORKDIR /calculator
RUN npm install
ENTRYPOINT [ "/bin/sh", "-c","npm start" ]
