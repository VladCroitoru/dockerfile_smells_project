FROM alpine:latest
ADD sabresume.sh /bin/
RUN chmod +x /bin/sabresume.sh
RUN apk update
RUN apk add curl jq bc grep
CMD ["/bin/sabresume.sh"]
