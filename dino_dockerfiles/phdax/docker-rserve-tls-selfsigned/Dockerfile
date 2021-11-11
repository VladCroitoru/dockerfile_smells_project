FROM rocker/r-base:latest

LABEL org.label-schema.license="GPL-2.0" \
      org.label-schema.vcs-url="https://github.com/phdax/docker-rserve-tls-selfsigned" \
      org.label-schema.vendor="" \
      maintainer="phdax <pophitdax@gmail.com>"

RUN apt-get update \
&& apt-get install -y --no-install-recommends \
      apt-utils \
      openssl \
      libssl-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& mkdir -p /opt/r/work \
&& openssl genrsa -out /opt/r/Rserve.key \
&& openssl req -new -key /opt/r/Rserve.key -out /opt/r/Rserve.csr -subj '/C=JP/ST=Tokyo/L=Tokyo/O=Example Ltd./OU=Web/CN=example.com/subjectAltName=test' \
&& openssl x509 -in /opt/r/Rserve.csr -days 3650 -req -signkey /opt/r/Rserve.key > /opt/r/Rserve.crt \
&& openssl x509 -in /opt/r/Rserve.crt -out /opt/r/Rserve.der -outform DER \
&& openssl x509 -in /opt/r/Rserve.der -inform DER -out /opt/r/Rserve.pem -outform pem

RUN wget -O /opt/r/Rserve.zip https://www.rforge.net/Rserve/snapshot/Rserve_1.8-6.tar.gz \
&& R CMD INSTALL /opt/r/Rserve.zip \
&& Rscript -e '.libPaths("./opt/r/lib")' \
&& rm -f /opt/r/Rserve.zip

COPY /conf/Rserv.conf /opt/r/
COPY /conf/user.txt /opt/r/

ENV R_LIBS="/opt/r/lib"

EXPOSE 6313

ENTRYPOINT R CMD Rserve --no-save --RS-conf /opt/r/Rserv.conf && tail -f /dev/null
