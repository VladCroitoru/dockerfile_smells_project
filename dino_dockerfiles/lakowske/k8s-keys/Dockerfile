FROM lachlanevenson/k8s-kubectl:latest

MAINTAINER Seth Lakowske <lakowske@gmail.com>

ENV CERTS=/certs

RUN apk add --update openssl bash tar && rm /var/cache/apk/*

ADD ./k8s-keys.sh /

RUN mkdir /certs
RUN chmod 755 /k8s-keys.sh

ENTRYPOINT ["/k8s-keys.sh"]
CMD /k8s-keys.sh
