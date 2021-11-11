FROM alpine
ADD script.sh /bin/
RUN chmod +x /bin/script.sh
RUN apk -Uuv add curl ca-certificates
ENTRYPOINT /bin/script.sh
