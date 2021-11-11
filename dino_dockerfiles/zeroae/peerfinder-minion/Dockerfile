FROM alpine:3.5
MAINTAINER Patrick Sodré

RUN apk add --no-cache bash curl
COPY script.sh script.sh

CMD [ "watch", "-n", "270", "-t", "/script.sh" ]
