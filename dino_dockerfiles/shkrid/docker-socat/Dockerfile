FROM alpine

LABEL maintainer "Artem Yasinskiy <shkrid@gmail.com>"

RUN apk add --no-cache socat 

COPY entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["/bin/entrypoint.sh"]
