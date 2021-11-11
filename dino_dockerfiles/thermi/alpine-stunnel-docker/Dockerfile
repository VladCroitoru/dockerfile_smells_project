FROM alpine
RUN apk --no-cache upgrade && apk --no-cache add stunnel ca-certificates
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/stunnel"]