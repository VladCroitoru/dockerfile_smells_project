FROM docker:17.12-dind

COPY docker.aai.com.crt  /certs/
RUN cat /certs/docker.aai.com.crt >> /etc/ssl/certs/ca-certificates.crt

RUN apk --update add \
    bash \
    openssh
CMD ["--insecure-registry", "docker.aai.com"]
