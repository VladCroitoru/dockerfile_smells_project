FROM alpine:3.12 as build
#we only need python for the mitmproxy addition
ENV SAUCE_VERSION 4.7.1

RUN apk update && apk add wget && rm -rf /var/cache/apk/*

RUN wget https://saucelabs.com/downloads/sc-$SAUCE_VERSION-linux.tar.gz -O - | tar -xz

RUN ls -la
RUN mkdir -p /out/bin && \
  cp sc-$SAUCE_VERSION-linux/bin/sc  /out/bin/ 

FROM python:3.8-slim-buster
LABEL maintainer="Caleb Jaquith (caleb.jaquith@tealium.com)"
COPY --from=build /out /usr/local

RUN apt-get update -qqy \
 && apt-get install -qqy \
      apt-utils ca-certificates \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install mitmproxy \
    && rm -rf ~/.cache/pip

ADD /certs/op_cert.crt /usr/local/share/ca-certificates/op_cert.crt

# 'convert' to .crt by changing the extension on copy
RUN mitmdump & sleep 5 && ls -l ~/.mitmproxy/
RUN cp ~/.mitmproxy/mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy-ca-cert.crt

RUN ls -l /usr/local/share/ca-certificates/
RUN chmod 644 /usr/local/share/ca-certificates/op_cert.crt && update-ca-certificates -v
RUN awk -v cmd='openssl x509 -noout -subject' ' /BEGIN/{close(cmd)};{print | cmd}' < /etc/ssl/certs/ca-certificates.crt

RUN ls -a ~/.mitmproxy

EXPOSE 4445
EXPOSE 8032

EXPOSE 8080

CMD ["--version"]

RUN echo '\n\nBuild successful!\n\n'

