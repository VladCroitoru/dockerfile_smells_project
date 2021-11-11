FROM docker.io/library/alpine:latest

ENV PORT 8080
EXPOSE $PORT

RUN apk add --no-cache curl nmap
ADD *.sh /

USER 4242
CMD [ "/dummy.sh" ]
