FROM alpine:3.4

RUN apk add --update \
  nodejs \
  && rm -rf /var/cache/apk/*

EXPOSE 80

# APPLICATION INSTALLATION
###########################
COPY app/ /app

# RUNTIME
#########
WORKDIR /app
CMD printf "\n[npm update]\n" ; npm update && printf "\n[ping-pong]\n" ; node .
