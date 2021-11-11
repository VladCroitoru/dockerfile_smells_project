FROM alpine
ADD main.sh /bin/
RUN chmod +x /bin/main.sh
RUN apk add --no-cache openssh
ENTRYPOINT /bin/main.sh
