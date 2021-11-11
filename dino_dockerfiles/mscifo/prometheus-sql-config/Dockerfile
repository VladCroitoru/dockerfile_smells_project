#Prometheus SQL Config Store Dockerfile
FROM alpine
LABEL maintainer "Matt Scifo (matt@scifo.info)"

RUN apk add --update git docker
COPY get-config.sh /get-config.sh
RUN chmod +x /get-config.sh

CMD ["/get-config.sh"]
