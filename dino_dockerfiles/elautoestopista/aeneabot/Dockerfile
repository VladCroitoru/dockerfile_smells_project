FROM alpine:latest

LABEL maintainer="sergio@fernandezcordero.net"

# Environment and dependencies
RUN apk update && \
    apk add bash python3 ca-certificates wget gcc python3-dev musl-dev libffi-dev openssl-dev && \
    update-ca-certificates && \
    rm -f /var/cache/apk/* && \
    rm /bin/sh && \
    ln -s /bin/bash /bin/sh && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    mkdir -p /opt/aenea && \
    addgroup aenea --gid 1001 && \
    adduser -g aenea -G aenea -h /opt/aenea -D aenea -u 1001 && \
    mkdir -p /opt/aenea/bot/
# Deploy
ADD aenea/* /opt/aenea/
RUN chown -R aenea:aenea /opt/aenea && \
    pip install -r /opt/aenea/requirements.txt
# Run
USER aenea
CMD python3 /opt/aenea/aenea.py
