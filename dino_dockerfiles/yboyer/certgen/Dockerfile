FROM alpine

COPY cfssl /usr/bin/
COPY cfssljson /usr/bin/
COPY gen /usr/bin/

WORKDIR /certs

RUN cfssl print-defaults config | sed 's/168h\|8760h/87800h/' > /ca-config.json

ENTRYPOINT ["gen"]
