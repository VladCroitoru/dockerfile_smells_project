FROM docker:18.04
RUN wget https://github.com/APNIC-net/crocker/releases/download/v0.2.0/crocker -O /usr/local/bin/crocker && \
    chmod 755 /usr/local/bin/crocker
ENTRYPOINT /usr/local/bin/crocker
