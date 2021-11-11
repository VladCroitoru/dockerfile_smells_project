FROM apereo/cas:v4.2.2

MAINTAINER Sergio Silva

COPY etc/cas.properties /etc/cas/cas.properties

COPY etc/thekeystore /etc/cas/jetty/

COPY etc/*.json /cas-overlay/src/main/resources/services/

CMD ["/cas-overlay/bin/run-jetty.sh"]