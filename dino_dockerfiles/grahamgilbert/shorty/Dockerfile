FROM alpine:3.7
RUN apk update && apk upgrade
RUN apk add --no-cache python3 ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
COPY shorty.py /usr/local/bin/shorty
RUN chmod 755 /usr/local/bin/shorty
COPY templates /opt/shorty/templates
CMD ["/usr/local/bin/shorty"]
