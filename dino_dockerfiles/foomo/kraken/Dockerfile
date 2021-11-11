FROM scratch

COPY bin/kraken-linux-amd64 /usr/sbin/kraken

# install ca root certificates
# https://curl.haxx.se/docs/caextract.html
# http://blog.codeship.com/building-minimal-docker-containers-for-go-applications/
#ADD https://curl.haxx.se/ca/cacert.pem /etc/ssl/certs/ca-certificates.crt
COPY docker/files/cacert.pem /etc/ssl/certs/ca-certificates.crt

EXPOSE 80

VOLUME /etc/kraken/config.yaml

ENTRYPOINT ["/usr/sbin/kraken"]
CMD ["--config=/etc/kraken/config.yaml"]