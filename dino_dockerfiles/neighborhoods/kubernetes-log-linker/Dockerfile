FROM alpine

RUN apk add --no-cache bash jq

COPY log-linker.sh /log-linker.sh
RUN chmod +x /log-linker.sh
CMD ["/log-linker.sh"]
