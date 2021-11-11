FROM unicon/shibboleth-idp:latest

ENV JETTY_MAX_HEAP=64m \
    JETTY_BROWSER_SSL_KEYSTORE_PASSWORD=password \
    JETTY_BACKCHANNEL_SSL_KEYSTORE_PASSWORD=password

COPY container_files/shibboleth-idp/ /opt/shibboleth-idp/
