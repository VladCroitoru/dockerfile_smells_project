FROM alpine:latest

RUN apk add --update npm && \
    npm i -g newman 

ENTRYPOINT [ "newman" ]
