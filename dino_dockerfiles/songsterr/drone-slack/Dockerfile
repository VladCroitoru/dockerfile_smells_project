FROM alpine:3.5

RUN apk add --no-cache curl

ADD script.sh /bin/
RUN chmod +x /bin/script.sh
ENTRYPOINT /bin/script.sh
