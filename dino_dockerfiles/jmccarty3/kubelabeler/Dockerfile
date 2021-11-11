FROM alpine
MAINTAINER jmccarty3@gmail.com

ENV KUBEMASTER_URL kubernetes
RUN apk update && apk add jq bash curl
ADD label.sh /label.sh

ENTRYPOINT ["/label.sh"]
